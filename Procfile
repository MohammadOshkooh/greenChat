web: daphne config.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=config.settings -v2

release: python manage.py migrate