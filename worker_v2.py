from driver_object import Selenium_object
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
from logger import Logger
from re import sub
from bs4 import BeautifulSoup
from math import ceil
from time import sleep

import settings

class Worker(Selenium_object):
    
    def __init__(self, window):
        # super().__init__()
        self.window = window
        self.top_url = "https://rabota.ua"
        self.password = settings.password
        self.email = settings.email
        self.user_logger = Logger().user_logger()
        self.dev_logger = Logger().dev_logger()
        self.count_vacancy_per_page = 40
        self.hrefs = []
        self.session = requests.session()
        self.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        self.session.max_redirects = 22
    def login(self):
        self.connect_to_service(self.top_url)
        #press on the log in btn
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class, 'santa-typo-secondary-bold profile-name ng-star-inserted')]"))).click()
        #find log in btn in the form of login
        self.sign_in_btn = self.driver.find_element(By.XPATH, "//button[contains(@class, 'primary-normal santa-block santa-typo-regular-bold full-width')]")

        self.email_input = self.driver.find_element(By.XPATH, "(//aside[contains(@class, 'sidebar')]//input[contains(@id, 'santa-input')])[1]")
        self.passwrod_input = self.driver.find_element(By.XPATH, "(//aside[contains(@class, 'sidebar')]//input[contains(@id, 'santa-input')])[2]")

        self.email_input.send_keys(settings.email)
        self.passwrod_input.send_keys(settings.password)
        
        self.sign_in_btn.click()
        try:
            #проверка успешно ли вошли в аккаунт
            self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//div[@id='mount_react_el']/section/div[contains(@class, 'fd-f-between-middle')]/a"
            )))
            self.dev_logger.info(f"Успешный вход на {self.top_url} используя - {settings.email} / {settings.password}")
            self.user_logger.info(f"Успешный вход на {self.top_url} используя - {settings.email} / {settings.password}")
        except Exception as err:
            try:
                #find an error msg
                err_msg = self.wait.until(EC.presence_of_element_located((
                            By.XPATH, "//santa-error-msg/p"
                    ))).text

                if err_msg.strip() in ['Поле обязательное для заполнения', 'Неверный формат адреса', 'Вы ввели неверный пароль или логин']:
                    self.dev_logger.warning(f"Ошибка {err_msg} при входе на {self.top_url} используя - {self.email}: {self.password}")
                    self.dev_logger.warning(f"Ошибка {err_msg} при входе на {self.top_url} используя - {self.email}: {self.password}")
                else:
                    self.dev_logger.warning(f"Неопознанная ошибка {err_msg} при входе на {self.top_url} используя - {self.email}: {self.password}")
                    self.dev_logger.warning(f"Неопознанная ошибка {err_msg} при входе на {self.top_url} используя - {self.email}: {self.password}")
            except Exception as err:
                self.dev_logger.critical(f"Ошибка {err}.Вход не был исполнен")
                self.user_logger.critical(f"Ошибка {err}.Вход не был исполнен")

    def get_data_of_search(self, url):
        try:
            response = requests.get(url)
        except:
            sleep(2)
            try:
                response = requests.get(url)
            except Exception as err:
                print(f'Some error with connect to site: {err}')
                return
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all('h2', class_='card-title')
            for num, item in enumerate(cards):
                href = item.find('a')['href']
                self.hrefs.append(href)
                # title = item.find('a')['title']
            if 'pg' not in url:
                count_vacancies = soup.select('#ctl00_content_vacancyList_ltCount > .fd-fat-merchant')[0].text
                pages = ceil(int(count_vacancies)/self.count_vacancy_per_page)
                return pages
            else:
                return
        else:
            print(f'Can not get the {url} with status code: {response.status_code}')

    def parse_data_vacancies(self, url):
        pages = self.get_data_of_search(url)
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
            sleep(1)
        return len(self.hrefs)
            

        

if __name__ == '__main__':
    Worker('window').parse_data_vacancies('https://rabota.ua/zapros/qa/украина/?scheduleId=1&profLevelIDs=5%2c4%2c3&agency=false')