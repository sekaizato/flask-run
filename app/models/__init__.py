# app/models/__init__.py

import uuid
from app.database.postgres import db

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: f'0x{str(uuid.uuid4()).replace("-", "")}')
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'