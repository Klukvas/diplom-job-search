# from sqlalchemy import create_engine, Column
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Integer, String, Float

# from scrapy.utils.project import get_project_settings

# DeclarativeBase = declarative_base()

# def db_connect():
#     return create_engine('sqlite:///diplom.db'),  pool_pre_ping=True)

# def create_table(engine):
#     DeclarativeBase.metadata.create_all(engine)

# class AbiturientRow(DeclarativeBase):
#    

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, create_database

from sqlalchemy.sql import select



Base = declarative_base()

class DataBaseClient:
    def __init__(self):
        self.engine = create_engine('sqlite:///diplom.db')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

db_client = DataBaseClient()

class Cities(Base):
    __tablename__ = 'Cities'
    city = Column(String(100),  primary_key=True, unique = True)

class EngLvl(Base):
    __tablename__ = 'EngLvl'
    lvl = Column(String(100),  primary_key=True, unique = True)

def insert_EngLvl():
    with open('engLvl.txt', encoding='utf-8') as f:
        print('start insert')
        for line in f:
            record = EngLvl(
                lvl = line.replace('\n', ' ')
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()
        print('finish insert')

def insert_cities():
    with open('rabota_ua_cites.txt', encoding='utf-8') as f:
        print('start insert')
        for line in f:
            record = Cities(
                city = line.replace('\n', ' ')
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()
        print('finish insert')

def get_all_engLvls():
    engLvls_objects = db_client.session.query(EngLvl).all()
    all_engLvls = []
    for object_ in engLvls_objects:
        all_engLvls.append(object_.lvl)
    return all_engLvls

def get_all_cities():
    cities_objects = db_client.session.query(Cities).all()
    all_cities = []
    for object_ in cities_objects:
        all_cities.append(object_.city)
    return all_cities

def get_filtered_cities(value):
    ch = str(value).capitalize()
    cities_objects = db_client.session.query(Cities).filter(Cities.city.like('{0}%'.format(ch)))
    filtered_cities = []
    for object_ in cities_objects:
        filtered_cities.append(object_.city)
    return filtered_cities

