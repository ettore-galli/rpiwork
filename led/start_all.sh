# Start switch server
python switchserver/app.py & 

# Start switch client
python -m http.server 8001 --directory ./switchclient/build & 


