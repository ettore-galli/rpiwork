import {
    getTodoListDatabase,
    addTodo,
    retrieveAllTodoItems
} from './database';


require("fake-indexeddb/auto");
const FDBFactory = require("fake-indexeddb/lib/FDBFactory");



describe('Todo Database', () => {
    const mockIndexedDB = new FDBFactory();
    it('should initialize', () => {
        getTodoListDatabase(mockIndexedDB).then((db) => {
            expect(db).toBeDefined()
        }).catch((error) => {
            fail("Initialization failed", error)
        })
    });

    it('should add an item', (done) => {
        const mockIndexedDB = new FDBFactory();
        getTodoListDatabase(mockIndexedDB).then((db) => {
            addTodo(db, { data: "test" }).then(() => {
                retrieveAllTodoItems(db).then((items) => {
                    expect(items).toStrictEqual([{ data: "test" }])
                })
                done()
            }).catch((error) => {
                done("Add Todo failed" + error)
            })
        })
    });
});
