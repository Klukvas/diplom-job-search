from sqlalchemy import Column, Integer
from Models.Base import Base, DataBaseClient

db_client = DataBaseClient()

class UserId(Base):
    __tablename__ = 'userId'
    id = Column(Integer(), primary_key=True)

def get_user_id():
    id_objects = db_client.session.query(UserId).all()
    ids = []
    for object_ in id_objects:
        ids.append(object_.id)
    return ids



def insert_id(id):
    record = UserId(
            id = id
            ) 
    db_client.session.merge(record)
    db_client.session.commit()

def delete_ids():
    db_client.session.query(UserId).delete()
    db_client.session.commit()