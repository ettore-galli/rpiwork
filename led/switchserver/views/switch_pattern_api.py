from flask import request, session, current_app, render_template
from flask.views import MethodView

class SwitchPatternApi(MethodView):

    def get(self):
        return """
Please make a POST request.

Some examples:

curl http://localhost:5000/pattern/ -X POST -H "Content-Type: application/json"  -d '{"pattern": [1,1,1,0], "duration": 0.5}'


"""

    def post(self):
        pattern = self.__prepare_led_pattern(request.json["pattern"])
        current_app.switch_driver.output_pattern(*pattern) 
        return request.json

    def __prepare_led_pattern(self, json_pattern):
        return [v for s, v in sorted(json_pattern.items())]

        
    
