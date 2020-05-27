from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
  """Base data model for all objects"""
  __abstract__ = True
    # define here __repr__ and json methods or any common method
    # that you need for all your models
  def __init__(self, **kargs):
    super().__init__(**kargs)