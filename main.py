from uvicorn import run

from user_management_py.db.connection import init_db

if __name__ == "__main__":
    init_db()
    run(
        "user_management_py.create_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True)
