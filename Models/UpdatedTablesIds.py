
from sqlalchemy import Column, Integer
from Models.Base import Base, DataBaseClient

db_client = DataBaseClient()

class UpdatedTablesIds(Base):
    __tablename__ = 'UpdatedTablesIds'
    upd_id = Column(Integer(),  primary_key=True, unique = True)

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