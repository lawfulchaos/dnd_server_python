import os

from dndserver import app

if __name__ == "__main__":
    app.run(port=os.environ.get("PORT", 5000))
