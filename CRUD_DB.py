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
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DATE
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, create_database

from sqlalchemy.sql import select
from datetime import date


Base = declarative_base()

class DataBaseClient:
    def __init__(self):
        self.engine = create_engine('mysql+mysqldb://root:sololane56457@localhost:3306/diplom?charset=utf8')
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

class Cities(Base):
    __tablename__ = 'Cities'
    city = Column(String(100),  primary_key=True, unique = True)

class EngLvl(Base):
    __tablename__ = 'EngLvl'
    lvl = Column(String(100),  primary_key=True, unique = True)

class Search_period(Base):
    __tablename__ = 'search_period'
    period = Column(String(100),  primary_key=True, unique = True)

class Heading(Base):
    __tablename__ = 'heading'
    heading = Column(String(100),  primary_key=True, unique = True)

class SendedCvs(Base):
    __tablename__ = 'sendedCvs'
    id = Column(Integer(), primary_key=True)
    vacancy_id = Column(Integer())
    company_id = Column(Integer())
    cv_id = Column(Integer())
    cv_name = Column(String(100))
    is_profCv = Column(Boolean(), unique=False)
    date_of_callback = Column(DATE(), default=date.today())

def insert_EngLvl():
    with open('data_for_db\engLvl.txt', encoding='utf-8') as f:
        print('start insert')
        for line in f:
            record = EngLvl(
                lvl = line.replace('\n', ' ')
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()
        print('finish insert')

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

def insert_period():
    with open('data_for_db\период_поискаю.txt', encoding='utf-8') as f:
        print('start insert')
        for line in f:
            record = Search_period(
                period = line.replace('\n', ' ').strip()
                                ) 
            db_client.session.merge(record)
        db_client.session.commit()
        print('finish insert')

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

def insert_sended_cvs(vacancy_id, company_id, cv_id, cv_name ,is_profCv):
    record = SendedCvs(
        vacancy_id = vacancy_id,
        company_id = company_id,
        cv_id = cv_id,
        cv_name = cv_name,
        is_profCv = is_profCv
                        ) 
    db_client.session.merge(record)
    db_client.session.commit()
    print('finish insert')

def get_all_engLvls():
    engLvls_objects = db_client.session.query(EngLvl).all()
    all_engLvls = []
    for object_ in engLvls_objects:
        all_engLvls.append(object_.lvl.strip())
    all_engLvls.reverse()
    return all_engLvls

def get_all_periods():
    periods_objects = db_client.session.query(Search_period).all()
    periods = []
    for object_ in periods_objects:
        periods.append(object_.period)
    return periods

def get_all_cities():
    cities_objects = db_client.session.query(Cities).all()
    all_cities = []
    for object_ in cities_objects:
        all_cities.append(object_.city.strip())
    all_cities.remove('Вся Украина')
    all_cities.insert(0, 'Вся Украина')
    return all_cities

def get_filtered_cities(value):
    ch = str(value).capitalize()
    cities_objects = db_client.session.query(Cities).filter(Cities.city.like('{0}%'.format(ch)))
    filtered_cities = []
    for object_ in cities_objects:
        filtered_cities.append(object_.city)
    return filtered_cities

def get_all_headings():
    heading_objects = db_client.session.query(Heading).all()
    headings = []
    for object_ in heading_objects:
        headings.append(object_.heading)
    headings.remove('Все рубрики')
    headings.insert(0, 'Все рубрики')
    return headings

def get_all_vacancies_ids():
    ids_object = db_client.session.query(SendedCvs.vacancy_id).all()
    all_ids = []
    for object_ in ids_object:
        all_ids.append(object_[0])
    return all_ids

def get_filtered_vacans(value):
    vacans_objects = db_client.session.query(SendedCvs).filter(SendedCvs.vacancy_id==value)
    filtered_vacans = []
    for object_ in vacans_objects:
        filtered_vacans.append(object_.vacancy_id)
    return filtered_vacans

def get_user(email, password):
    user_exists = db_client.session.query(UserInfo).filter(UserInfo.email==email, UserInfo.password==password)
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

def insert_user(email, password):
    record = UserInfo(
                    email = email.strip(),
                    password=password.strip(),
                    confirmed=True
                                    ) 
    db_client.session.merge(record)
    db_client.session.commit()

