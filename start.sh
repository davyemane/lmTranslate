
#!/bin/bash
PORT=${PORT:-8000}
uvicorn app:app 0.0.0.0:$PORT
