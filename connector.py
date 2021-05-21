import requests
import json

host = 'http://127.0.0.1:5000'

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

def get_engLvls_conn():
    url = f"{host}/get_engLvls"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['all_engLvls']

def get_headings_conn():
    url = f"{host}/get_headings"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['headings']

def get_cities_conn():
    url = f"{host}/get_cities"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['all_cities']

def get_periods_conn():
    url = f"{host}/get_periods"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data['periods']
