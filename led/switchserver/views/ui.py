from flask import request, session, current_app, render_template
from flask.views import MethodView

class Ui(MethodView):
 
    def get(self):
        return self.__prepare_index_page()


    def post(self):
        return self.__prepare_index_page()

    def __prepare_index_page(self):
        response = render_template("index.html")
        # response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
        # response.headers['Cache-Control'] = 'public, max-age=0'
        return response
