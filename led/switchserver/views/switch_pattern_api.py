from flask import request, session, current_app, render_template
from flask.views import MethodView

class SwitchPatternApi(MethodView):

    def get(self):
         return {}
        
    def post(self):
        input_pattern = request.json["pattern"]
        current_app.status_manager.set_whole_status(self.__prepare_status(input_pattern))
        pattern = self.__prepare_led_pattern(
            current_app.status_manager.get_whole_status()
        )
        current_app.switch_driver.set_output_pattern(*pattern) 
        return request.json

    def __prepare_status(self, json_pattern):
        return [(s, v) for s, v in sorted(json_pattern.items())]

    def __prepare_led_pattern(self, status):
       return [v for s, v in status]
        
    
