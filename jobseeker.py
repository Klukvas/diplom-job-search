import requests
import json
from datetime import datetime
from Models.SendedCvs import insert_sended_cvs
from re import search
class Jobseeker:
    def __init__(self):
        self.auth_url = "https://auth-api.rabota.ua"
        self.main_url = 'https://api.rabota.ua'

    def login(self, username, password):
        url = f"{self.auth_url}/Login"
        payload = json.dumps({
            "username": f"{username}",
            "password": f"{password}"
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.text.replace('"', '')
        else:
            return None

    def get_cv_site(self, token):
        url = f"{self.main_url}/account/jobsearch/cvlist"
        payload={}
        headers = {
        'Authorization': f'Bearer {token}'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        return data

    def get_cv_downloaded(self, token):
        url = f"{self.main_url}/account/jobsearch/attachlist"
        payload={}
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.request("POST", url, headers=headers, data=payload)
        data = json.loads(response.text)
        return data
    
    def get_cv_by_name_flag(self, name, flag, token):
        possible_cv = []
        id_from_few_cvs = ''
        if flag:
            all_resumes = self.get_cv_site(token)
            if len(all_resumes) > 1:
                for cv in all_resumes:
                    if cv['speciality'].strip().lower() == name.strip().lower():
                        possible_cv.append(cv)
                if len(possible_cv) == 0:
                    return 'error'
                elif len(possible_cv) == 1:
                    return possible_cv[0]['resumeId']
                elif len(possible_cv) > 1:

                    max = datetime(1900, 5, 17, 1, 1, 1, 1)
                    for num, cv in enumerate(possible_cv):
                        correct_date = datetime.strptime(
                            cv['addDate'].replace('T', ' '),
                            '%Y-%m-%d %H:%M:%S.%f'
                        )
                        if correct_date > max:
                            max = correct_date
                            id_from_few_cvs = cv['resumeId']
                    return id_from_few_cvs

            elif len(all_resumes) == 0:
                return 'error'
            elif len(all_resumes) == 1:
                cvId = all_resumes[0]['resumeId']
        else:
            all_resumes = self.get_cv_downloaded(token)
            if len(all_resumes) > 1:
                for cv in all_resumes:
                    if cv['fileName'].strip().lower() == name.strip().lower():
                        possible_cv.append(cv)
                if len(possible_cv) == 0:
                    return 'error'
                elif len(possible_cv) == 1:
                    return possible_cv[0]['id']
                elif len(possible_cv) > 1:

                    max = datetime(1900, 5, 17, 1, 1, 1, 1)
                    for num, cv in enumerate(possible_cv):
                        correct_date = datetime.strptime(
                            cv['lastSentDate'].replace('T', ' '),
                            '%Y-%m-%d %H:%M:%S.%f'
                        )
                        if correct_date > max:
                            max = correct_date
                            id_from_few_cvs = cv['id']
                    return id_from_few_cvs

            elif len(all_resumes) == 0:
                return 'error'
            elif len(all_resumes) == 1:
                cvId = all_resumes[0]['id']

    def vacancy_has_question(self, vacancyId):
        url = f"{self.main_url}/vacancy/questions?id={vacancyId}"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        if len(data):
            if data[0]['name'] == "Укажите уровень владения следующим языком":
                if data[0]['languageName'] == 'Английский':
                    return ['succsess', data[0]['id']]
                else:
                    return ['error1', data[0]['languageName']]
            else:
                return ['error2', data[0]['name']]
        else:
            return None

    def apply(self, token, addAlert, vacancyId, letter, eng_lvl, profCv, nameCv, href):
        #profCv - резюме сделано на сайте или загруженно вручную
        cvId = self.get_cv_by_name_flag(nameCv, profCv, token)
        if cvId == 'error':
            return 'errorCv'
        else:
            url = f"{self.main_url}/vacancy/apply"
            question = self.vacancy_has_question(vacancyId)
            payload = {
                "addAlert": addAlert,
                "name": "test",
                "lastName": "test",
                "email": "programmer56457@gmail.com",
                "vacancyId": vacancyId,
                "cvId": cvId,
                "letter": f"{letter}",
                "profCv": profCv
                }
            if question == None:
                pass
            elif question[0] == 'succsess':
                payload['cQuestExp'] = []
                payload['cQuestLang'] = [f'{question[1]}-{eng_lvl}']
            else:
                return False

            headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
            payload = json.dumps(payload)
            response = requests.request("POST", url, headers=headers, data=payload)

            responce = json.loads(response.text)
            if responce['success']:
                company_id = search(r'company\d+', href).group(0).replace('company', '')
                insert_sended_cvs(vacancyId, company_id, cvId, nameCv, profCv)
            return responce['success']



