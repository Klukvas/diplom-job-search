from sqlalchemy import Column, Integer, String
import json
from Models.Base import Base, DataBaseClient

db_client = DataBaseClient()
class EngLvl(Base):
    __tablename__ = 'EngLvl'
    lvl = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = True)

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