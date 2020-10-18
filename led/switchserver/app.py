from flask import Flask, request, session
from views.switch_pattern_api import SwitchPatternApi
from views.ui import Ui
from multiswitch.multiswitch_driver import SwitchDriver
from switchserver.status_manager.status_manager import StatusManager

def get_application_config():
    # TODO: Load from external configuration
    return {
        "host" : "0.0.0.0",
        "port" : 8080,
        "static_folder" : "static",
        "secret_key" : b'_5#y2L"F4Q8z\n\xec]/'
        }

def create_app():
    app = Flask(__name__)
    map_views(app)

    cfg = get_application_config()
     
    for attr, value in cfg.items():
        print ("Setting {} to {}".format(str(attr), str(value)))
        setattr(app, attr, value)

    app.port=80 
    app.switch_driver = SwitchDriver(None)     
    app.status_manager = StatusManager(app.switch_driver.get_switches())  
    return app

def map_views(app):
    app.add_url_rule('/pattern/', view_func=SwitchPatternApi.as_view('pattern'))
    app.add_url_rule('/', view_func=Ui.as_view('ui'))

app = create_app()

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    cfg = get_application_config()
    app.run(host=cfg["host"], port=cfg["port"])
        
    


 
