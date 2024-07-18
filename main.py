from app import app
from config import Setting

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=Setting.host, port=Setting.port)