import os
from flask import Flask

app = Flask(__name__)

# app root
app_root = os.path.dirname(app.instance_path)

# Get config
app.config.from_object('config')

@app.route("/")
def home():
    return app_root
