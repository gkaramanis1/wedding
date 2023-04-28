import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://wedding:cngw@192.168.1.94:3306/wedding'#os.environ.get('SQLALCHEMY_DATABASE_URI')
