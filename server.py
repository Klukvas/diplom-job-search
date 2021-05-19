from flask import Flask
from flask import request
import json
from CRUD_DB_server import *
app = Flask(__name__)


@app.route('/get_user', methods=['GET'])
def get_user():
    email = request.args.get('email')
    password = request.args.get('password')
    if email == None:
        return json.dumps({'result':0, 'message': 'Email parameter is required'})
    elif password == None:
        return json.dumps({'result':0, 'message': 'Password parameter is required'})
    else:
        user = get_user_db(email, password)
        return json.dumps({'result':1, 'user': user})

@app.route('/create_user', methods=['POST'])
def create_user():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    if email == None:
        return json.dumps({'result':0, 'message': 'Email parameter is required'})
    elif password == None:
        return json.dumps({'result':0, 'message': 'Password parameter is required'})
    else:
        insert_user(email, password)
        return json.dumps({'result':1})

@app.route('/get_emails', methods=['GET'])
def get_emails():
    emails = get_all_emails()
    return json.dumps({'result':1, 'emails': emails})

@app.route('/get_engLvls', methods=['GET'])
def get_engLvls():
    all_engLvls = get_all_engLvls()
    return json.dumps({'all_engLvls': all_engLvls}, ensure_ascii=False)

@app.route('/get_headings', methods=['GET'])
def get_headings():
    headings = get_all_headings()
    return json.dumps({'headings': headings}, ensure_ascii=False)


@app.route('/get_cities', methods=['GET'])
def get_cities():
    all_cities = get_all_cities()
    return json.dumps({'all_cities': all_cities}, ensure_ascii=False)

@app.route('/get_periods', methods=['GET'])
def get_periods():
    periods = get_all_periods()
    return json.dumps({'periods': periods}, ensure_ascii=False)










app.run()