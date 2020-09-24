import os

basedir = os.path.abspath(os.path.dirname(__file__))

acc_date = ""


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "db/demo.sqlite3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "my_secret_key"

    JSON_AS_ASCII = False


def gvar_init():
    global acc_date
    acc_date = ""
