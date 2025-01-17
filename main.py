from uvicorn import run

if __name__ == "__main__":
    run(
        "user_management_py.create_app:app",
        host="0.0.0.0",
        port=8000,
        reload=True)
