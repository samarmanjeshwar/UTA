from flask import Flask
import sys
from app import app, db
print(app)
print(db)
sys.path.insert(1, "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages")
from flask_mongoengine import MongoEngine
