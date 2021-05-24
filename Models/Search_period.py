from sqlalchemy import Column, Integer, String
import json
from Models.Base import Base, DataBaseClient

db_client = DataBaseClient()

class Search_period(Base):
    __tablename__ = 'search_period'
    period = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = False, default=0)

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
