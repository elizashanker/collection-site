import datetime
import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

class Object(SqlAlchemyBase, UserMixin):
    __tablename__ = 'objects'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, nullable=True)
    creation_year = Column(Integer)
    creation_history = Column(String)
    creation_place = Column(String)
    collection_history = Column(String)
    materials = Column(String)
    photos = Column(String)
    series_id = Column(String)