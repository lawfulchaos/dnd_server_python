import os

from dndserver import app

if __name__ == "__main__":
    print("Starting app")
    app.run(port=os.environ.get("PORT", 5000))
    print("App started")