import uvicorn
from config import Config

from routes import app

if __name__ == '__main__':
    uvicorn.run(
        app,
        host=Config.HOST,
        port=Config.PORT,
    )