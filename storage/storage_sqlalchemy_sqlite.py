from storage.storage import _Storage

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PickleType
from sqlalchemy.orm import sessionmaker
import pickle

Base = declarative_base()

class Data(Base):
    """
    Model for data.
    """
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True, nullable=False)
    url = Column(String(254), unique=True, nullable=False)
    data = Column(PickleType)

class Storage(_Storage):
    def __init__(self):
        self.engine = create_engine('sqlite:///../data/data.sqlite')
        # create a configured "Session" class
        self.Session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)

    def get(self, url: str) -> dict:
        # create a Session
        session = self.Session()
        # query data
        db_result = session.query(Data).selectfirst(Data.c.url == url)
        db_data = dict()
        if db_result is not None:
            db_data['url'] = url
            db_data['data'] = pickle.loads(db_result.data)
            return db_data

        return None


    def save(self, pickle_data: dict):
        # create a Session
        session = self.Session()
        try:
            # Check if already exist in db
            db_data = session.query(Data).selectfirst(Data.c.url == pickle_data['url'])

            if db_data is None: # no data in db
                db_data = Data()
                db_data.url = pickle_data['url']
                db_data.data = pickle.dumps(pickle_data['data'])
                session.flush()
            else: # data exist in db - update
                db_data.data = pickle.dumps(pickle_data['data'])
                session.flush()
            session.commit()
        except:
            session.rollback()
