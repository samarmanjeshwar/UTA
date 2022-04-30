import os
class Config(object):
  SECRETKEY = os.urandom(24)
  WTF_CSRF_SECRET_KEY = os.urandom(24)
  MONGODB_SETTINGS = {'db': 'UTA_Enrollment',
    'host': 'mongodb+srv://samarmanjeshwar:samdps1234@cluster0.kqzwp.mongodb.net/UTA_Enrollment?retryWrites=true&w=majority'}

