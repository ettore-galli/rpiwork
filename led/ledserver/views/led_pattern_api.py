from flask import request, session, current_app, render_template
from flask.views import MethodView

class LedPatternApi(MethodView):

    def get(self):
        return """
Please make a POST request.

Some examples:

curl http://localhost:5000/pattern/ -X POST -H "Content-Type: application/json"  -d '{"pattern": [1,1,1,0], "duration": 0.5}'


"""
    def get(self):
        return render_template("index.html")

    def post(self):
        pattern = [int(t) for t in request.json["pattern"]]
        duration = request.json["duration"]
        current_app.led_driver.output_pattern(*pattern) 
        return request.json
