from app import app
import os

@app.route("/")
def index():

    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a container behind nginx."

    return "hello from flask"