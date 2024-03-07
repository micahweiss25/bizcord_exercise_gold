During development: `python server.py`

On production: `gunicorn -b :5000 --threads 1 server:app`