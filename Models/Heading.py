from sqlalchemy import Column, Integer, String
import json

from Models.Base import Base, DataBaseClient

db_client = DataBaseClient()

class Heading(Base):
    __tablename__ = 'heading'
    heading = Column(String(100),  primary_key=True, unique = True)
    weight = Column(Integer(), unique = False, default=0)

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