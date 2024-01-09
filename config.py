import os

# get the base directory of this folder
basedir = os.path.abspath(os.path.dirname(__file__))

# 'C:\\Users\\rcord\\Documents\\codingtemple-kekambas-137\\week6\\FLASK_API'

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///' + os.path.join(basedir, 'app.db')