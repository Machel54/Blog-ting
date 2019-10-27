import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://machel:jkl@localhost/blog'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}