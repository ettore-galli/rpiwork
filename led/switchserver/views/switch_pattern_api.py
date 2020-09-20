from flask import request, session, current_app, render_template
from flask.views import MethodView

class SwitchPatternApi(MethodView):

    def get(self):
        return {"s{}".format(str(i)):bool(status) for i, status in enumerate(current_app.switch_driver.get_output_pattern())}

    def post(self):
        pattern = self.__prepare_led_pattern(request.json["pattern"])
        current_app.switch_driver.set_output_pattern(*pattern) 
        return request.json

    def __prepare_led_pattern(self, json_pattern):
        return [v for s, v in sorted(json_pattern.items())]

        
    
