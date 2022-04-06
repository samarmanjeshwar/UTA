import os

class Config(object):
  SECRET+KY = os.environ.get("SECRET_KEY") or "qwerty"

