from collections import deque
import threading
import connector
from datetime import datetime
class TheardsContent:
    def __init__(self) -> None:
        self.q = deque()
    async def create_theards(self):
        allPeriods = threading.Thread(target=connector.get_periods_conn, args=(self.q,))
        all_variants = threading.Thread(target=connector.get_headings_conn, args=(self.q,))
        all_engLvls = threading.Thread(target=connector.get_engLvls_conn, args=(self.q,))
        all_cities = threading.Thread(target=connector.get_cities_conn, args=(self.q,))
        n1 = datetime.now()
        all_cities.start()
        all_cities.join()

        all_engLvls.start()
        all_engLvls.join()

        all_variants.start()
        all_variants.join()

        allPeriods.start()
        allPeriods.join()
        n2 = datetime.now()
        print(f'N2 - N1: {n2-n1}')
        # all_periods = connector.get_periods_conn()
        # self.period_search.addItems(all_periods)

        # all_variants = connector.get_headings_conn()
        # self.variants.addItems(all_variants)

        # all_cities = connector.get_cities_conn()
        # self.city.addItems(all_cities)

        # all_engLvls = connector.get_engLvls_conn()
        # self.eng_lvl.addItems(all_engLvls)
TheardsContent().create_theards()
# n3 = datetime.now()
# q = []
# all_periods = connector.get_periods_conn(q)
# all_variants = connector.get_headings_conn(q)
# all_cities = connector.get_cities_conn(q)
# all_engLvls = connector.get_engLvls_conn(q)
# n4 = datetime.now()
# print(f'N4 - N3: {n4-n3}')