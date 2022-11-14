
from datetime import datetime
from extensions import db


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(70), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    images = db.Column(db.String(100), nullable=False)
    logo_id = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
