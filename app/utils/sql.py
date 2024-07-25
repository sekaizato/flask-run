# app/services/utils.py

from sqlalchemy.inspection import inspect

def to_dict(model):
    """Convert SQLAlchemy model to dictionary"""
    return {c.key: getattr(model, c.key) for c in inspect(model).mapper.column_attrs}