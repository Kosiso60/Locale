from app import app
from config import config


env = 'development'  
app.config.from_object(config[env])

if __name__ == '__main__':
    app.run()
