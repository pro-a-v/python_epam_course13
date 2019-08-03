from storage.storage import Storage

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PickleType

Base = declarative_base()

class Data(Base):
    """
    Model for data.
    """
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String(254), unique=True, nullable=False)
    data = Column(PickleType)

class Stor(Storage):
    def __init__(self):
        pass