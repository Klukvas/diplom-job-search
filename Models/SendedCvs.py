from sqlalchemy import Column, Integer, String, Boolean, DATE
from datetime import date
import json
from Models.Base import Base, DataBaseClient

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