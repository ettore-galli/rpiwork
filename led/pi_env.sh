export VIRTUALENV_ACTIVATE=./venv/bin/activate
export FLASK_ENV=development
export PYTHONPATH=$PYTHONPATH:$(pwd)/..
export REACT_APP_SWITCH_SERVER_ENDPOINT=http://$(hostname):8080/pattern/