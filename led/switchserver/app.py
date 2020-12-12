from flask import Flask
from flask_cors import CORS
from views.switch_pattern_api import SwitchPatternApi
from views.ui import Ui
try:
    from multiswitch.multiswitch_driver import SwitchDriver
except Exception:
    from multiswitch.multiswitch_driver_mock \
        import SwitchDriverMock as SwitchDriver
from switchserver.status_manager.status_manager import StatusManager


def get_application_config():
    # TODO: Load from external configuration
    return {
        "host": "0.0.0.0",
        "port": 8080,
        "static_folder": "static",
        "secret_key": b'_5#y2L"F4Q8z\n\xec]/'
    }


def create_app():
    app = Flask(__name__)
    CORS(app)
    map_views(app)

    cfg = get_application_config()

    for attr, value in cfg.items():
        print("Setting {} to {}".format(str(attr), str(value)))
        setattr(app, attr, value)

    app.port = 80
    app.switch_driver = SwitchDriver(None)
    app.status_manager = StatusManager(
        prepare_switch_status(
            app.switch_driver.get_switches()
        )
    )
    return app


def prepare_switch_status(switch_list):
    return [("s{}".format(str(i+1)), 0) for i in range(len(switch_list))]


def map_views(app):
    app.add_url_rule(
        '/pattern/', view_func=SwitchPatternApi.as_view('pattern'))
    app.add_url_rule('/', view_func=Ui.as_view('ui'))


app = create_app()

# @app.after_request
# def add_header(r):
#     r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
#     r.headers["Pragma"] = "no-cache"
#     r.headers["Expires"] = "0"
#     r.headers['Cache-Control'] = 'public, max-age=0'
#     r.headers['Access-Control-Allow-Origin'] = '*'
#     return r


if __name__ == "__main__":
    cfg = get_application_config()
    app.run(host=cfg["host"], port=cfg["port"])
