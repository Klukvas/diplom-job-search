import requests
import json

host = 'https://auto-job-searsh-erver.herokuapp.com/'

def create_user_conn(email, password):
    url = f"{host}/create_user"
    payload = json.dumps({
    "email": f"{email}",
    "password": f"{password}"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

def synchronized_vacans_conn(vacans_ovjects, id):
    url = f"{host}/sunchronize"
    payload = json.dumps({
        "vacans_object": vacans_ovjects,
        "id": id
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text

def get_user_conn(email, password):
    url = f"{host}/get_user?email={email}&password={password}"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


def get_emails_conn():
    url = f"{host}/get_emails"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response.text

def get_engLvls_conn(*args):
    if args:
        url = f"{host}/get_engLvls?all=all"
    else:
        url = f"{host}/get_engLvls"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        if not args:
            data = json.loads(response.text)
            return data['all_engLvls']
        else:
            return response.text
    else:
        return 'error'
    

def get_headings_conn(*args):
    if args:
        url = f"{host}/get_headings?all=all"
    else:
        url = f"{host}/get_headings"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        if not args:
            data = json.loads(response.text)
            return data['headings']
        else:
            return response.text
    else:
        return 'error'
    

def get_cities_conn(*args):
    if args:
        url = f"{host}/get_cities?all=all"
    else:
        url = f"{host}/get_cities"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        if args:
            return response.text
        else:
            data = json.loads(response.text)
            return data['all_cities']
    else:
        return 'error'
    

def get_periods_conn(*args):
    if args:
        url = f"{host}/get_periods?all=all"
    else:
        url = f"{host}/get_periods"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        if not args:
            data = json.loads(response.text)
            return data['periods']
        else:
            return response.text
    else:
        return 'error'
    
def get_updated_data_conn():
    url = f"{host}/get_updated_data"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']
    else:
        return 'error'