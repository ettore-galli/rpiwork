'use strict';

const dbName = "TodoListDatabase";
const dbVersion = 1;

function performDbInitialization(db) {
    let objectStore = db.createObjectStore("todos", { autoIncrement: true });
    return objectStore;
}

export function getTodoListDatabase(idb) {
    return new Promise((resolve, reject) => {
        let request = idb.open(dbName, dbVersion);
        request.onupgradeneeded = (event) => {
            let db = event.target.result;
            performDbInitialization(db);
        }
        request.onerror = function (event) {
            reject(event.target);
        };
        request.onsuccess = function (event) {
            resolve(event.target.result);
        };
    })
}


export function bulkInsert(db, records) {
    return new Promise(
        (resolve, reject) => {
            let transaction = db.transaction(["todos"], "readwrite");
            let todoObjectStore = transaction.objectStore("todos");
            records.forEach((item) => {
                todoObjectStore.add(item)
            })
            transaction.commit();
            transaction.oncomplete = (event) => {
                resolve(event.target.result)
            }
            transaction.onerror = (event) => {
                reject(event.target)
            }
        }
    )
}

export function retrieveTodoItemByKey(db, key) {
    return new Promise(
        (resolve, reject) => {
            let todoObjectStore = db.transaction(["todos"], "readonly").objectStore("todos").get(key)
            todoObjectStore.onsuccess = (event) => {
                resolve(event.target.result)
            }
            todoObjectStore.onerror = (event) => {
                reject(event.target)
            }
        }
    )
}

export function retrieveAllTodoItems(db) {
    return new Promise(
        (resolve, reject) => {
            let todoObjectStore = db.transaction(["todos"], "readonly").objectStore("todos").getAll()
            todoObjectStore.onsuccess = (event) => {
                resolve(event.target.result)
            }
            todoObjectStore.onerror = (event) => {
                reject("Error retrieving list")
            }
        }
    )
}

export function updateTodo(db, item, key) {
    return new Promise(
        (resolve, reject) => {
            let todoObjectStore = db.transaction(["todos"], "readwrite").objectStore("todos").put(item, key)
            todoObjectStore.onsuccess = (event) => {
                resolve(event.target.result)
            }
            todoObjectStore.onerror = (event) => {
                reject("Update failed")
            }
        }
    )
}

export function addTodo(db, item) {
    return new Promise(
        (resolve, reject) => {
            let todoObjectStore = db.transaction(["todos"], "readwrite").objectStore("todos").add(item)
            todoObjectStore.onsuccess = (event) => {
                resolve(event.target.result)
            }
            todoObjectStore.onerror = (event) => {
                reject("Update failed")
            }
        }
    )
}

const demoTodos = [
    { title: "Item 1", details: "Todo list item # 1" },
    { title: "Item 2", details: "Todo list item # 2" },
    { title: "Item 3", details: "Todo list item # 3 (last one?)" }
];


/*
getTodoListDatabase(window.indexedDB).then((db) => {
    bulkInsert(db, demoTodos)
    return db
}).then(
    (db) => {
        retrieveTodoItemByKey(db, 2)
            .then(r => console.log(r))
        return db
    }
).then(
    (db) => {
        updateTodo(db, { title: "aggiornato", details: "voce aggiornata" }, 2)
            .then(r => console.log(r))
    }
)
*/
/*

var db;
var request = indexedDB.open("MyTestDatabase");
request.onerror = function (event) {
    console.log("Why didn't you allow my web app to use IndexedDB?!");
};
// This event is only implemented in recent browsers
request.onupgradeneeded = function (event) {
    // Save the IDBDatabase interface
    var db = event.target.result;

    // Create an objectStore for this database
    var objectStore = db.createObjectStore("customers", { keyPath: "ssn" });
    var objStore = db.createObjectStore("names", { autoIncrement: true });

    objectStore.createIndex("name", "name", { unique: false });
    objectStore.createIndex("email", "email", { unique: true });

    objectStore.transaction.oncomplete = (event) => {

        var customerObjectStore = db.transaction("customers", "readwrite").objectStore("customers");
        var namesObjectStore = db.transaction("names", "readwrite").objectStore("names")

        customerData.forEach(function (customer) {
            customerObjectStore.add(customer);
            console.log("add", customer)
        });

        customerData.forEach(function (customer) {
            namesObjectStore.add(customer.name);
        });
    }
};
request.onsuccess = function (event) {
    db = event.target.result;
    console.log(db)
};


const customerData = [
    { ssn: "444-44-4444", name: "Bill", age: 35, email: "bill@company.com" },
    { ssn: "555-55-5555", name: "Donna", age: 32, email: "donna@home.org" }
];

*/