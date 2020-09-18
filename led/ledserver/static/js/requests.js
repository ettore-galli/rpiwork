"use strict"

const requests = function (w){ 

    w.setSwitchPattern = function (pattern){
        axios.post('/pattern/', {
            firstName: 'Fred',
            lastName: 'Flintstone'
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
    }        
}

requests(window);


