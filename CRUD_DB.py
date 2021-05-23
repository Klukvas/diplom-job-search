from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Boolean, DATE, text
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, create_database

from sqlalchemy.sql import select
from datetime import date
import connector
import json

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

class RememeredData(Base):
    __tablename__ = 'RememeredData'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    email = Column(String(100))
    password = Column(String(100))

def insert_rememeredData(email, password):
    record = RememeredData(
            email = email,
            password = password
            ) 
    db_client.session.merge(record)
    db_client.session.commit()
    print('finish insert')

def get_rememeredData():
    data_object = db_client.session.query(RememeredData).all()
    data = []
    for object_ in data_object:
        data.append(object_.email)
        data.append(object_.password)
    return data

def delete_rememeredData():
    db_client.session.query(RememeredData).delete()
    db_client.session.commit()

class UserId(Base):
    __tablename__ = 'userId'
    id = Column(Integer(), primary_key=True)
def get_user_id():
    id_objects = db_client.session.query(UserId).all()
    ids = []
    for object_ in id_objects:
        ids.append(object_.id)
    return ids

class SendedCvs(Base):
    __tablename__ = 'sendedCvs'
    id = Column(Integer(), primary_key=True)
    vacancy_id = Column(Integer())
    company_id = Column(Integer())
    cv_id = Column(Integer())
    cv_name = Column(String(100))
    is_profCv = Column(Boolean(), unique=False)
    date_of_callback = Column(DATE(), default=date.today())
    synchronized = Column(Boolean(), unique=False, default=False)

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

def insert_id(id):
    record = UserId(
            id = id
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

def get_unsynchronized_vacans():
    vacans_objects = db_client.session.query(SendedCvs).filter(SendedCvs.synchronized==False)
    unsynchronized_vacans = []
    for object_ in vacans_objects:
        vacan_info = json.dumps({
            "id":  object_.id,
            "vacancy_id": object_.vacancy_id,
            "company_id": object_.company_id,
            "cv_id": object_.cv_id,
            "cv_name": object_.cv_name,
            "is_profCv": object_.is_profCv,
            "date_of_callback": object_.date_of_callback.isoformat()
            })

        unsynchronized_vacans.append(vacan_info)
    return unsynchronized_vacans

def upd_sync(id):
    db_client.session.query(SendedCvs).\
        filter(SendedCvs.id==id).\
        update({'synchronized': True})
    db_client.session.commit()

def delete_ids():
    db_client.session.query(UserId).delete()
    db_client.session.commit()

def create_all_tables():
    Base.metadata.create_all(db_client.engine)
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

class UpdatedTablesIds(Base):
    __tablename__ = 'UpdatedTablesIds'
    upd_id = Column(Integer(),  primary_key=True, unique = True)

def sync_cities(data):
    print(data)
    db_client.session.query(Cities).delete()
    db_client.session.commit()
    data = json.loads(data)['all_cities']
    for i in data:
        record = Cities(
            city = i['city'],
            weight = i['weight']
        )
        db_client.session.merge(record)
    db_client.session.commit()

def sync_periods(data):
    db_client.session.query(Search_period).delete()
    db_client.session.commit()
    data = json.loads(data)['periods']
    for i in data:
        record = Search_period(
            period = i['period'],
            weight = i['weight']
        )
        db_client.session.merge(record)
    db_client.session.commit()

def sync_headings(data):
    db_client.session.query(Heading).delete()
    db_client.session.commit()
    data = json.loads(data)['headings']
    for i in data:
        record = Heading(
            heading = i['heading'],
            weight = i['weight']
        )
        db_client.session.merge(record)
    db_client.session.commit()

def sync_engLvls(data):
    db_client.session.query(EngLvl).delete()
    db_client.session.commit()
    data = json.loads(data)['all_engLvls']
    for i in data:
        record = EngLvl(
            lvl = i['lvl'],
            weight = i['weight']
        )
        db_client.session.merge(record)
    db_client.session.commit()

def get_updated_ids():
    ids_object = db_client.session.query(UpdatedTablesIds).all()
    all_ids = []
    for object_ in ids_object:
        all_ids.append(object_.upd_id)
    return all_ids

def insert_updId(id):
    record = UpdatedTablesIds(upd_id = id) 
    db_client.session.merge(record)
    db_client.session.commit()

def get_all_periods(*args):
    periods_objects = db_client.session.query(Search_period).order_by(Search_period.weight.desc())
    periods = []
    if not args:
        for object_ in periods_objects:
            periods.append(object_.period)
    else:
        for object_ in periods_objects:
            periods.append(
                    {
                        "period": object_.period,
                        "weight": object_.weight
                    }
                )
    return periods

async def get_all_cities(*args):
    cities_objects = db_client.session.query(Cities).order_by(Cities.weight.desc())
    all_cities = []
    if not args:
        for object_ in cities_objects:
            all_cities.append(object_.city.strip())
    else:
        for object_ in cities_objects:
            all_cities.append({
                'city': object_.city.strip(),
                "weight":  object_.weight
            })
    return all_cities

def get_all_headings(*args):
    heading_objects = db_client.session.query(Heading).order_by(Heading.weight.desc())
    headings = []
    if not args:
        for object_ in heading_objects:
            headings.append(object_.heading)
    else:
        for object_ in heading_objects:
            headings.append({
                "heading": object_.heading,
                "weight":  object_.weight
            })
    return headings

def get_all_engLvls(*args):
    engLvls_objects = db_client.session.query(EngLvl).order_by(EngLvl.weight.desc())
    all_engLvls = []
    if not args:
        for object_ in engLvls_objects:
            all_engLvls.append(object_.lvl.strip())
    else:
        for object_ in engLvls_objects:
            all_engLvls.append({
                "lvl": object_.lvl.strip(),
                "weight":  object_.weight
            })
    return all_engLvls

def sync_ui_data():
    new_data = connector.get_updated_data_conn()
    print(f'new_data: {new_data}')
    all_ids = get_updated_ids()
    if new_data == 'error':
        pass
    else:
        for i in new_data:
            table_name = i['table_name']
            id = i['id']
            if id not in all_ids:
                if table_name == 'city':
                    result = connector.get_cities_conn(table_name)
                    sync_cities(result)
                elif table_name == 'search_period':
                    result = connector.get_periods_conn(table_name)
                    sync_periods(result)
                elif table_name == 'heading':
                    result = connector.get_headings_conn(table_name)
                    sync_headings(result)
                elif table_name == 'englvl':
                    result = connector.get_engLvls_conn(table_name)
                    sync_engLvls(result)
            insert_updId(id)