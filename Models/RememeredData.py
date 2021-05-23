from sqlalchemy import Column, Integer, String
from Models.Base import Base, DataBaseClient

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