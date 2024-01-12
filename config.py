import os
from dotenv import load_dotenv


# get the base directory of this folder
basedir = os.path.abspath(os.path.dirname(__file__))

# 'C:\\Users\\rcord\\Documents\\codingtemple-kekambas-137\\week6\\FLASK_API'

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')