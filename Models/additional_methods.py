import connector
from Models.Cities import sync_cities
from Models.Search_period import sync_periods
from Models.Heading import sync_headings
from Models.EngLvl import sync_engLvls
from Models.Base import Base, DataBaseClient
from Models.UpdatedTablesIds import get_updated_ids, insert_updId
db_client = DataBaseClient()


def create_all_tables():
    Base.metadata.create_all(db_client.engine)

def sync_ui_data():
    new_data = connector.get_updated_data_conn()
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