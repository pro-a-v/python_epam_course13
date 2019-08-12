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
        db_result = session.query(Data).filter_by(url = url)
        db_data = dict()
        db_data['url'] = url
        if db_result.count() > 0:
            db_data['data'] = pickle.loads(db_result.one().data)
        else:
            db_data['data'] = 'No data in DB, try to \'get\' it first'

        return db_data


    def save(self, pickle_data: dict):
        # create a Session
        session = self.Session()
        try:
            # Check if already exist in db
            db_data = session.query(Data).filter_by(url = pickle_data['url'])

            if db_data.count() == 0:# no data in db
                db_data_new = Data()
                db_data_new.url = pickle_data['url']
                db_data_new.data = pickle.dumps(pickle_data['data'])
                session.add(db_data_new)
                session.flush()
            else: # data exist in db - update
                record = db_data.one()
                record.data = pickle.dumps(pickle_data['data'])
                session.flush()
            session.commit()
        except:
            session.rollback()
