from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import secure_filename
import os
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def save_images(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        return file.save(os.path.join(Config.UPLOAD_FOLDER, filename))

