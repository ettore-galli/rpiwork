from flask import render_template
from flask.views import MethodView


class Ui(MethodView):

    def get(self):
        return self.__prepare_index_page()

    def post(self):
        return self.__prepare_index_page()

    def __prepare_index_page(self):
        return render_template("index.html")
