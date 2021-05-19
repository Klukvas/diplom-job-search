from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DATE, text
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


class SendedCvs(Base):
    __tablename__ = 'sendedCvs'
    id = Column(Integer(), primary_key=True)
    vacancy_id = Column(Integer())
    company_id = Column(Integer())
    cv_id = Column(Integer())
    cv_name = Column(String(100))
    is_profCv = Column(Boolean(), unique=False)
    date_of_callback = Column(DATE(), default=date.today())

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
