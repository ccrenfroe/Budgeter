from flask_app import app
from dotenv import load_dotenv
import os
load_dotenv()

# TODO: Do not use in deployment environment!
if __name__ == "__main__":
    app.run(port=os.getenv('PORT',8000))