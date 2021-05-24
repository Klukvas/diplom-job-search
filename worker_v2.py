import requests
from logger import Logger
from re import sub, search
from bs4 import BeautifulSoup
from math import ceil
from time import sleep
from jobseeker import Jobseeker
from Models import SendedCvs


class Worker:
    def __init__(self, window):
        self.window = window
        self.top_url = "https://rabota.ua"
        self.count_vacancy_per_page = 40
        self.seekerApi = Jobseeker()
        self.hrefs = []
        self.session = requests.session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        self.session.max_redirects = 22

    def get_data_of_search(self, url):
        try:
            response = requests.get(url)
        except:
            sleep(2)
            try:
                response = requests.get(url)
            except Exception as err:
                self.window.work_log.append(f'Some error with connect to site: {err}')
                return
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            count_vacancies = soup.select('#ctl00_content_vacancyList_ltCount > .fd-fat-merchant')[0].text
            if int(count_vacancies) >= 1:
                cards = soup.find_all('h2', class_='card-title')
                for num, item in enumerate(cards):
                    href = item.find('a')['href']
                    self.hrefs.append(href)
                    # title = item.find('a')['title']
                if 'pg' not in url:
                    pages = ceil(int(count_vacancies)/self.count_vacancy_per_page)
                    return pages
            else:
                return None
        else:
            self.window.work_log.append(f'Can not get the {url} with status code: {response.status_code}')

    def parse_data_vacancies(self, url):
        pages = self.get_data_of_search(url)
        if pages == None:
            pass
        else:
            for page in range(2, pages+1):
                if 'pg' in url:
                    url = sub(r'pg\d+', f'pg{page}', url)
                else:
                    if '?' in url:
                        parts_url = url.split('?')
                        parts_url.insert(1, f'/pg{page}')
                        parts_url[-1] = '?' + parts_url[-1]
                        url = ''.join(parts_url)
                    else:
                        url = url + f'/pg{page}'
                
                self.get_data_of_search(url)
        return len(self.hrefs)
            
    def send_cv(self, email, password, addAlert, letter, eng_lvl, profCv, nameCv):
        if not self.window.resend.isChecked():
            self.all_ids = SendedCvs.get_all_vacancies_ids()
        token = self.seekerApi.login(email, password)
        if token == None:
            yield 'LoginError'
        else:
            for href in self.hrefs:
                vacancyId = search(r'vacancy\d+', href).group(0).replace('vacancy', '')
                if not self.window.resend.isChecked():
                    if int(vacancyId) in self.all_ids:
                        yield ['AlreadySened', href]
                        continue
                    result = self.seekerApi.apply(token, addAlert, vacancyId, letter, eng_lvl, profCv, nameCv, href)
                    yield [result, href]
                else:
                    result = self.seekerApi.apply(token, addAlert, vacancyId, letter, eng_lvl, profCv, nameCv, href)
                    yield [result, href]

