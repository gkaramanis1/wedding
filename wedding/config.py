import os

class Config:
    #os.environ.get
    SECRET_KEY = ('random12345!')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wedding:cngw@localhost:3306/wedding'#os.environ.get('SQLALCHEMY_DATABASE_URI')
