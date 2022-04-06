from flask import Flask

app = Flask(__name__)
print(app)
from app import routes

if __name__ == "__main__":
  print(app)
  app.run()
