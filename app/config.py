from flask import Flask

app = Flask(__name__)


class Config:
    DEBUG = False
    

class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
}
