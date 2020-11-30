from driver_object import Selenium_object
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from logger import Logger

from bs4 import BeautifulSoup

from time import sleep

import settings

class Rabota_ua_robot:
    
    def __init__(self):
        self.selenium_object = Selenium_object()
        self.driver = self.selenium_object.driver
        self.top_url = "https://rabota.ua"
        self.wait = self.selenium_object.wait
        self.user_logger = Logger().user_logger()
        self.dev_logger = Logger().dev_logger()
        self.count_reponses = 0

    def end_work(self):
        self.driver.quit()

    def connect_to_service(self, url, *args):
        if len(args) == 0:
            try:
                self.driver.get(url)
            except Exception as err:
                self.dev_logger.warning(err)
                sleep(13)
                self.connect_to_service(url, 1)
        else:
            if args[0] == 1:
                try:
                    self.driver.get(url)
                except Exception as err:
                    self.dev_logger.warning(err)
                    sleep(13)
                    self.connect_to_service(url, 2)
            else:
                try:
                    self.driver.get(url)
                except Exception as err:
                    self.dev_logger.critical(f"{err}\n Не удалось подключиться к {url}. Завершение работы с сайтом {self.top_url}")
                    self.user_logger.critical(f"Не удалось подключиться к {url}. Завершение работы с сайтом {self.top_url}")
                    self.end_work()
                    #закончить работу

    def try_login(self):
        self.connect_to_service(self.top_url)
        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//a[contains(@class, 'f-header-menu-list-link-with-border')]/label"))).click()
        self.sign_in_btn = self.driver.find_element(By.XPATH, "//a[contains(@id, 'ctl00_Sidebar_login_lnkLogin')]")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@id, 'ctl00_Sidebar_login_lnkLogin')]")))
        self.email_input = self.driver.find_element(By.XPATH, "//input[contains(@id, 'ctl00_Sidebar_login_txbLogin')]")
        self.passwrod_input = self.driver.find_element(By.XPATH, "//input[contains(@id, 'ctl00_Sidebar_login_txbPassword')]")
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
                #проверка указан ли в правильном формате имейл
                self.err_msg = self.wait.until(EC.presence_of_element_located((
                    By.XPATH, "//div[contains(@id, 'divSidebarName')]/span[contains(@class, 'error-message')]"
                        ))).text
                self.dev_logger.warning(f"Ошибка {err} в формате имейла при входе на {self.top_url} используя - {settings.email}")
                self.dev_logger.warning(f"Ошибка  в формате имейла при входе на {self.top_url} используя - {settings.email}")
            except Exception as err:
                try:
                    #проверка зареган ли пользователь с такими данными
                    self.err_msg = self.driver.find_element(
                        By.XPATH, "//div[contains(@id, 'ctl00_content_ZoneLogin_pLogin')]/strong"
                    ).text
                    self.dev_logger.warning(f"Ошибка {err} при попытке входа на {self.top_url}  используя - {settings.email} / {settings.password}")
                    self.user_logger.warning(f"Ошибка при попытке входа на {self.top_url}  используя - {settings.email} / {settings.password}")
                except Exception as err:
                    self.dev_logger.critical(f"Ошибка {err} в формате имейла при входе на {self.top_url} завершение работы с данным сервисом")
                    self.user_logger.critical(f"Ошибка  в формате имейла при входе на {self.top_url} завершение работы с данным сервисом")

    def search(self):
        self.try_login()
        self.work_pos = self.driver.find_element(
            By.XPATH, "//div[contains(@class, 'styles__newheader-input-block-keyword___2cbFH')]/input[contains(@class, 'ui-autocomplete-input')]"
            )
        self.work_pos.send_keys(settings.keywords_for_search)
        self.region_input = self.driver.find_element(
            By.XPATH, "//div[contains(@class, 'styles__newheader-input-block-region___3qbhV')]/input[contains(@class, 'ui-autocomplete-input')]"
            )
        self.region_input.click()
        self.region_input.send_keys(Keys.BACKSPACE)
        self.region_input.send_keys(settings.region_of_searsh)
        #Без задержки в 3 секунды вместо введеного региона выбирается все регионы (обработка js-скрипта)
        sleep(3)
        self.region_input.send_keys(Keys.ENTER)
        
    def count_job_pages(self):
        self.search()
        try:
            #нахождение макс страниц
            max_pages = self.driver.find_elements(
                By.XPATH, "//dl[contains(@class, 'f-text-royal-blue fd-merchant f-pagination')]/dd/a"
            )
            return max_pages[-2].text 
        except Exception as err:
            #переход в этот блок значит что или найдена 1 страница или не найдено результатов
            self.count_vacancies = self.driver.find_element(
                By.XPATH, "//span[contains(@class, 'fd-fat-merchant')]"
            ).text
            if int(self.count_vacancies) == 0:
                self.dev_logger.warning(f"Ошибка {err} в поиске вакансий на {self.top_url}.По запросу - {settings.keywords_for_search} \ {settings.region_of_searsh}. Завершение работы с данным сервисом")
                self.user_logger.warning(f"Ошибка {err} в поиске вакансий на {self.top_url}.По запросу - {settings.keywords_for_search} \ {settings.region_of_searsh}. Завершение работы с данным сервисом")
                return 0

            else:
                return 1 
    
    def bs4_parse(self, item):
        soup = BeautifulSoup(item, 'html.parser')
        try:
            info_vacans = soup.find('div', class_='card-main-content').find('p', class_='card-title').find('a', class_='ga_listing')
            href = self.top_url + info_vacans.get('href') 
            title = info_vacans.get('title')
            return {title: href}
        except Exception as err:
            #Ошибка возникает если есть больше одной страници с вакансиями
            return None
            
    def get_links_by_page(self):
        job_links = []
        self.all_vacansies_by_page = self.driver.find_elements(
                By.XPATH, "//table[@id='ctl00_content_vacancyList_gridList']/tbody/tr"
            )
        for item in self.all_vacansies_by_page:
            dict_ = self.bs4_parse(item.get_attribute('innerHTML'))
            if dict_ != None:
                job_links.append(dict_)
        return job_links

    def get_job_links(self):
        self.count_pages = self.count_job_pages()
        job_links_by_all_pages = []
        if self.count_pages == 0:
            #ниодной вакансии нет
            self.dev_logger.warning(f"Ошибка {err} в поиске вакансий на {self.top_url}.По запросу - {settings.keywords_for_search} \ {settings.region_of_searsh}. Завершение работы с данным сервисом ")
            self.user_logger.warning(f"Ошибка в поиске вакансий на {self.top_url}.По запросу - {settings.keywords_for_search} \ {settings.region_of_searsh}. Завершение работы с данным сервисом")
            self.end_work()
        elif self.count_pages == 1:
            #найдена только 1 страница с вакансиями
            job_links_dic = self.get_links_by_page()
        else:
            for item in range(1, int(self.count_pages) + 1):
                #цикл от первой страници с вакансиями до максимальной ( последней )
                if item == 1:
                    #если это первая страница
                    job_links_by_all_pages = self.get_links_by_page()
                else:
                    try:
                        #в полседующих страницах ( [2:] ) в url добавляется /pg{page_number}
                        curr_url = str(self.driver.current_url)
                        if "pg" in curr_url:
                            #создаем новый url для след.страници путем /pg{ 'номер итерации в цикле' }
                            curr_url = curr_url.split('/')[3:-1]
                            curr_url.append(f'pg{item}')
                            next_url = self.top_url + '/' +'/'.join(curr_url)
                        else:
                            next_url = curr_url + f'/pg{item}'
                        self.connect_to_service(next_url)
                        job_links_by_all_pages += self.get_links_by_page()
                    except Exception as err:
                        self.dev_logger.warning(f"Ошибка {err} при настройке url на сервисе {self.top_url}")
                        self.user_logger.warning(f"Ошибка при настройке url на сервисе {self.top_url}")
        #возвращаем списко состоящий из словарей( пара -  Название вакасии:ссылка на неё )
        return job_links_by_all_pages                  
    
    def make_response_form_1(self, title):
        #находим кнопку на странице вакансии для переходя на форму отправки резюме
        btn_send_cv = self.driver.find_elements(
            By.XPATH, "//div[contains(@class, 'santa-py-20 santa-flex santa-justify-between')]//button[contains(@class, 'primary-large santa-block santa-typo-regular-bold')]"
        )
        try:
            btn_send_cv[0].click()
        except:
            try:
                self.driver.refresh()
                btn_send_cv[1].click()
            except:
                self.dev_logger.warning(f"Ошибка {err} не удалось нажать на кнопку перехода к форме отправки резюме на сервисе {self.top_url}")
                self.user_logger.warning(f"Ошибка не удалось нажать на кнопку перехода к форме отправки резюме на сервисе {self.top_url}")

        #ветка - выбрать резюме созданное на сайте или выбрать ранее отправленное  
        if settings.cv_on_site == True:
            #Находит все резюме, созданные на сайт
            cv_on_site_block = self.driver.find_elements(
                By.XPATH, "//*[@id='ctl00_content_ngElementWrapper_vacancyApplyForm_rdBtnLstResumeList']//span"
            )
            count_cvs = len(cv_on_site_block)
            cv_found = False
            for num, cv in enumerate(cv_on_site_block):
                if cv.text.strip().lower() == settings.name_cv.strip().lower():
                    cv.click()
                    cv_found = True
                    break
                else:
                    if int(count_cvs) == int(num):
                        self.dev_logger.warning(f"Резюме не найдено сервисе {self.top_url}. Окончание работы с сервисом")
                        self.user_logger.warning(f"Резюме не найдено сервисе {self.top_url}. Окончание работы с сервисом")
                        self.end_work()

            if cv_found:
                #Если желаемое резюме найдено, проверяем есть ли сопроводительное письмо
                if len(settings.ad_letter.strip()) > 0:
                    ad_letter_btn = self.driver.find_element(
                            By.XPATH, "//a[contains(@class, 'fd-craftsmen')]/span[contains(@class, 'f-text-dark-bluegray')]"
                            ).click()
                    self.driver.find_element(
                        By.XPATH, '//*[@id="ctl00_content_ngElementWrapper_vacancyApplyForm_txAreaGreeting"]'
                        ).send_keys(settings.ad_letter.strip())
                try:
                    #Проверяем есть ли блок с выставлением уровня англ
                    self.driver.find_element(
                        By.XPATH, f"//select[contains(@id, 'ctl00_content_ngElementWrapper_vacancyApplyForm_applyControlQuestion_rptLanguages_ctl00_ddlSkills')]"
                    ).click()
                    sleep(4)
                    self.driver.find_element(
                        By.XPATH, f"//*[@id='ctl00_content_ngElementWrapper_vacancyApplyForm_applyControlQuestion_rptLanguages_ctl00_ddlSkills']/option[@value='3']"
                    ).click()
                except Exception as err:
                    #Нету блока с уровнем англ
                    pass
                if not settings.send_to_email:
                    self.driver.find_element(
                        By.XPATH, "//div[contains(@id, 'ctl00_content_ngElementWrapper_vacancyApplyForm_plhSendMail')]//span[contains(@class, 'fd-craftsmen')]"
                    ).click()
                self.driver.find_element(
                    By.XPATH, "//a[contains(@id, 'ctl00_content_ngElementWrapper_vacancyApplyForm_hpLnkSendResumeToEmployer')]"
                ).click()
                self.wait.until(EC.element_to_be_clickable((
                    By.XPATH, "//a[contains(@class, 'f-btn-primary fd-beefy-soldier')]"
                )))
                self.count_reponses += 1
                self.dev_logger.info(f"Успешный отзыв на вакансию {title}: {self.driver.current_url}")
                self.user_logger.info(f"Успешный отзыв на вакансию {title}: {self.driver.current_url}")
                return

    def make_response_form_2(self, title):
        #находим кнопку на странице вакансии для переходя на форму отправки резюме
        btn_send_cv = self.driver.find_elements(
            By.XPATH, "//button[contains(@class, 'primary-large santa-block santa-typo-regular-bold full-width')]"
        )
        try:
            btn_send_cv[0].click()
        except:
            try:
                self.driver.refresh()
                btn_send_cv[1].click()
            except Exception as err:
                self.dev_logger.warning(f"Ошибка {err} не удалось нажать на кнопку перехода к форме отправки резюме на сервисе {self.top_url}")
                self.user_logger.warning(f"Ошибка не удалось нажать на кнопку перехода к форме отправки резюме на сервисе {self.top_url}")

        #ветка - выбрать резюме созданное на сайте или выбрать ранее отправленное  
        if settings.cv_on_site == True:
            #Находит все резюме, созданные на сайт
            cv_on_site_block = self.driver.find_elements(
                By.XPATH, "//santa-radio-group[contains(@class, 'santa-text-black-700 santa-block ng-untouched ng-pristine ng-valid')]//p[contains(@class, 'santa-typo-regular')]"
            )
            count_cvs = len(cv_on_site_block)
            cv_found = False
            for num, cv in enumerate(cv_on_site_block):
                if cv.text.strip().lower() == settings.name_cv.strip().lower():
                    cv.click()
                    cv_found = True
                    break
                else:
                    if int(count_cvs) == int(num):
                        self.dev_logger.warning(f"Резюме не найдено сервисе {self.top_url}. Окончание работы с сервисом")
                        self.user_logger.warning(f"Резюме не найдено сервисе {self.top_url}. Окончание работы с сервисом")
                        self.end_work()
            if cv_found:
                #Если желаемое резюме найдено, проверяем есть ли сопроводительное письмо
                if len(settings.ad_letter.strip()) > 0:
                    ad_letter_btn = self.driver.find_elements(
                            By.XPATH, "//p[contains(@class, 'santa-ml-10 santa-typo-regular-bold santa-text-black-500')]"
                            )[0].click()
                    sleep(2)
                    self.driver.find_element(
                        By.XPATH, '//*[@id="cover-letter"]'
                        ).send_keys(settings.ad_letter.strip())
                try:
                    #Проверяем есть ли блок с выставлением уровня англ
                    self.driver.find_element(
                        By.XPATH, f"//span[contains(@class, 'santa-inline-block santa-py-10 santa-px-20 santa-cursor-pointer ng-star-inserted')]"
                    ).click()
                    sleep(4)
                    self.driver.find_element(
                        By.XPATH, f"//ul[contains(@class, 'santa-p-0 santa-m-0 santa-list-none ng-star-inserted')]/li[contains(text(), {settings.eng_level})]"
                    ).click()
                except Exception as err:
                    #Блок с уровнем англ отсутствует
                    pass
                if not settings.send_to_email:
                    self.driver.find_element(
                        By.XPATH, "//div[contains(@class, 'checkbox-wrap')]"
                    ).click()
                self.driver.find_element(
                    By.XPATH, "//santa-button[contains(@class, 'santa-block santa-relative santa-flex-grow')]"
                ).click()
                self.count_reponses += 1
                self.dev_logger.info(f"Успешный отзыв на вакансию {title}: {self.driver.current_url}")
                self.user_logger.info(f"Успешный отзыв на вакансию {title}: {self.driver.current_url}")
                return

    def make_response_to_vanancy(self, title):
        #Есть несколько вариантов прогрузки формы для отклика 
        try:
            self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//span[contains(@class, 'santa-text-blue-500 santa-typo-regular')]"
            )))
            self.make_response_form_1(title)
        except:
            self.wait.until(EC.element_to_be_clickable((
                By.XPATH, "//figcaption[contains(@class, 'santa-pl-10 santa-typo-regular-bold santa-text-red-500')]"
            )))
            self.make_response_form_2(title)

    def go_to_the_vacancy(self):
        dict_of_jobs = self.get_job_links()
        #print(len(dict_of_jobs))
        if len(dict_of_jobs) > 0:
            for item in dict_of_jobs:
                title = list(item.keys())[0]
                href = list(item.values())[0]
                self.connect_to_service(href)
                #Если кнопка "отправить резюме" ведет на сайт компании - вакансию пропускаем
                try:
                    go_to_company_site = self.driver.find_element(
                        By.XPATH, 
                        "//p[contains(@class, 'santa-mt-10 santa-text-center santa-typo-additional santa-text-black-700')]"
                        )
                    vacans_url = self.drive.current_url.split('?')[0]
                    self.dev_logger.info(f"Кнопка 'отправить резюме' ведет на сайт компании - вакансию пропускаем {title}: {vacans_url}")
                    self.user_logger.info(f"Кнопка 'отправить резюме' ведет на сайт компании - вакансию пропускаем {title}: {vacans_url}")
                    continue
                except:
                    self.make_response_to_vanancy(title)
rr = Rabota_ua_robot()
rr.go_to_the_vacancy()    
    