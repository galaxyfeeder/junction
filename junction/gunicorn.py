command = '/webapps/junction/env/bin/gunicorn'
pythonpath = '/webapps/junction/junction'
logfile = '/webapps/junction/logs/gunicorn.log'
bind = '0.0.0.0:8000'
workers = 3
