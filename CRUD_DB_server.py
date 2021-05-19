from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DATE, text
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, create_database

from sqlalchemy.sql import select
from datetime import date
import json
# Cities.__table__.create(DataBaseClient().engine)

Base = declarative_base()

class DataBaseClient:
    def __init__(self):
        self.engine = create_engine('mysql+mysqldb://root:sololane56457@localhost:3306/server?charset=utf8')
        # self.engine = create_engine('sqlite:///diplom.db')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

db_client = DataBaseClient()

class UserInfo(Base):
    __tablename__ = 'userinfo'
    email = Column(String(100),  primary_key=True, unique = True)
    password = Column(String(100),  primary_key=True, unique = True)
    confirmed = Column(Boolean(), unique=False, default=False)
    chat_id = Column(Integer())

class EngLvl(Base):
    __tablename__ = 'EngLvl'
    lvl = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = True)

class Search_period(Base):
    __tablename__ = 'search_period'
    period = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = False, default=0)

class Heading(Base):
    __tablename__ = 'heading'
    heading = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = False, default=0)

class Cities(Base):
    __tablename__ = 'Cities'
    city = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = False, default=0)


def insert_heading():
    with open('data_for_db\parents.txt', encoding='utf-8') as f:
        print('start insert')
        for line in f:
            record = Heading(
                heading = line.replace('\n', ' ').strip()
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()
        print('finish insert')

def insert_period():
    with open('data_for_db\период_поискаю.json', encoding='utf-8') as f:
        print('start insert')
        data = json.load(f)
        for per in data.items():
            record = Search_period(
                period = per[0].replace('\n', ' ').strip(),
                weight = per[1]
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()
        print('finish insert')

def insert_EngLvl():
    with open('data_for_db\engLvl.json', encoding='utf-8') as f:
        data = json.load(f)
        for lvl in data.items():
            record = EngLvl(
                lvl = lvl[0].replace('\n', ' '),
                weight = lvl[1]
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()

def insert_user(email, password):
    record = UserInfo(
                    email = email.strip(),
                    password=password.strip(),
                    confirmed=True
                                    ) 
    db_client.session.merge(record)
    db_client.session.commit()

def insert_cities():
    with open('data_for_db\cities.txt', encoding='utf-8') as f:
        print('start insert')
        for line in f:
            record = Cities(
                city = line.replace('\n', ' ')
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()
        print('finish insert')


def get_all_periods():
    periods_objects = db_client.session.query(Search_period).order_by(Search_period.weight.desc())
    periods = []
    for object_ in periods_objects:
        periods.append(object_.period)
    return periods

def get_all_cities():
    cities_objects = db_client.session.query(Cities).order_by(Cities.weight.desc())
    all_cities = []
    for object_ in cities_objects:
        all_cities.append(object_.city.strip())
    all_cities.remove('Вся Украина')
    all_cities.insert(0, 'Вся Украина')
    return all_cities

def get_all_headings():
    heading_objects = db_client.session.query(Heading).order_by(Heading.weight.desc())
    headings = []
    for object_ in heading_objects:
        headings.append(object_.heading)
    headings.remove('Все рубрики')
    headings.insert(0, 'Все рубрики')
    return headings

def get_all_engLvls():
    engLvls_objects = db_client.session.query(EngLvl).order_by(EngLvl.weight.desc())
    all_engLvls = []
    for object_ in engLvls_objects:
        all_engLvls.append(object_.lvl.strip())
    all_engLvls.reverse()
    return all_engLvls

def get_user_db(email, password):
    user_exists = db_client.session.query(UserInfo).filter(text(f"UserInfo.email like binary '{email}' and UserInfo.password like binary '{password}'"))

    user = []
    for object_ in user_exists:
        user.append(object_.confirmed)
    return user

def get_all_emails():
    user_exists = db_client.session.query(UserInfo).all()
    user = []
    for object_ in user_exists:
        user.append(object_.email)
    return user