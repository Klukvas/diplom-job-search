from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from settings import *
Base = declarative_base()

class DataBaseClient:
    def __init__(self):
        self.engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}:{port}/{db_name}?charset=utf8')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

