from flask import Flask, request, session
from views.led_pattern_api import LedPatternApi
from multiled.multiled_driver import LedDriver

def create_app():
    app = Flask(__name__)
    app.add_url_rule('/pattern/', view_func=LedPatternApi.as_view('pattern'))
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.led_driver = LedDriver(None)     
 
    return app

app = create_app()
      

 

@app.before_request
def before_request_func():
    pass
        
    


 
