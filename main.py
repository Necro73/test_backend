import uvicorn
from app.modules.fast_api_module.fast_api_module import app

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1:8000")