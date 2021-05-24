from sqlalchemy import  Column, Integer, String
import json

from Models.Base import Base, DataBaseClient
db_client = DataBaseClient()
class Cities(Base):
    __tablename__ = 'Cities'
    city = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = False, default=0)

def sync_cities(data):
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

def get_all_cities(*args):
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