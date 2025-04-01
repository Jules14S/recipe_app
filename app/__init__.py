from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app():
    load_dotenv()
    app = Flask(__name__)

    # Config
    UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
        f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app import routes
    routes.init_routes(app)

    return app
