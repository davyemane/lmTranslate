
#!/bin/bash
PORT=${PORT:-8000}
python manage.py runserver 0.0.0.0:$PORT