from uvicorn import run

from user_management_py.create_app import app

if __name__ == "__main__":
    run(
        "user_management_py.create_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True)
