from flask import request, session, current_app, render_template
from flask.views import MethodView

class Ui(MethodView):
 
    def get(self):
        return render_template("index.html")
    

    def post(self):
        print (request.values)
        return render_template("index.html")
