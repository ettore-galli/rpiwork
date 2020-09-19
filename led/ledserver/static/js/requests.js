"use strict"

const requests = function (w){ 

    w.performSetSwitchPatternRequest = function (pattern){
        axios.post('/pattern/', pattern)
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
    }        
}

requests(window);


