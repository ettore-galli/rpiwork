from flask import Flask, request, session
from views.led_pattern_api import LedPatternApi
from views.ui import Ui
from multiled.multiled_driver import LedDriver

def create_app():
    app = Flask(__name__)
    map_views(app)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.static_folder='static'
    app.host='0.0.0.0'
    app.port='5000'
    app.led_driver = LedDriver(None)     
 
    return app

def map_views(app):
    app.add_url_rule('/pattern/', view_func=LedPatternApi.as_view('pattern'))
    app.add_url_rule('/', view_func=Ui.as_view('ui'))

app = create_app()

@app.before_request
def before_request_func():
    pass
        
    


 
