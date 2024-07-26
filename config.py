import os

class Config(object):
    ENV_VAR = "Y"
    # SQL_ALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/dbname'
    # SQLALCHEMY_DATABASE_URI = 'postgres://admin:password@localhost:5432/sekai'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:password@localhost/sekai'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
