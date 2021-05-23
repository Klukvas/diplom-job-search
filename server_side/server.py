from flask import Flask
from flask import request
import json
from CRUD_DB_server import *
import asyncio

app = Flask(__name__)


@app.route('/get_user', methods=['GET'])
async def get_user():
    email = request.args.get('email')
    password = request.args.get('password')
    if email == None:
        return json.dumps({'result':0, 'message': 'Email parameter is required'})
    elif password == None:
        return json.dumps({'result':0, 'message': 'Password parameter is required'})
    else:
        user = await get_user_db(email, password)
        return json.dumps({'result':1, 'user': user})

@app.route('/create_user', methods=['POST'])
async def create_user():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']
    if email == None:
        return json.dumps({'result':0, 'message': 'Email parameter is required'})
    elif password == None:
        return json.dumps({'result':0, 'message': 'Password parameter is required'})
    else:
        resp = await insert_user(email, password)
        if resp:
            id = await get_userId_db(email, password)
            return json.dumps({'result':1, 'id': id})
        else:
            return json.dumps({'result':0})

@app.route('/get_emails', methods=['GET'])
async def get_emails():
    emails = await get_all_emails()
    return json.dumps({'result':1, 'emails': emails})

@app.route('/get_engLvls', methods=['GET'])
async def get_engLvls():
    all_engLvls = await get_all_engLvls()
    return json.dumps({'all_engLvls': all_engLvls}, ensure_ascii=False)

@app.route('/get_headings', methods=['GET'])
async def get_headings():
    headings = await get_all_headings()
    return json.dumps({'headings': headings}, ensure_ascii=False)

@app.route('/get_cities', methods=['GET'])
async def get_cities():
    all_cities = await get_all_cities()
    return json.dumps({'all_cities': all_cities}, ensure_ascii=False)

@app.route('/get_periods', methods=['GET'])
async def get_periods():
    periods = await get_all_periods()
    return json.dumps({'periods': periods}, ensure_ascii=False)

@app.route('/sunchronize', methods=['POST'])
async def sunchronize():
    request_data = request.get_json()
    vacans_object = request_data['vacans_object']
    id = request_data['id']
    upd_ids = await insert_vacans(vacans_object, id)
    return json.dumps({'upd_ids': upd_ids}, ensure_ascii=False)
if __name__ == '__main__':
    app.run()