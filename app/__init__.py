from flask import Flask
from config import Config
import os

import sys
sys.path.insert(1, "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages")

from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = os.urandom(24)
db = MongoEngine()
db.init_app(app)

print(app.config)

from app import routes
if  __name__ == "__main__":
  debug = True
  app.run()

