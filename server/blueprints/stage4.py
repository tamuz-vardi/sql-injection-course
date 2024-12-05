from flask import Flask, render_template, redirect, request, session, url_for, Blueprint, session
from flask_session import Session
import logging

from mysql.connector.errors import ProgrammingError

from ..consts import DEFAULT_PORT, DEFAULT_HOST, PROJECT_ROOT
from ..utils.mysql import create_cursor
from ..utils.general import get_file_contents

stage4_bp = Blueprint("stage4", __name__)

USERS_TABLE = 'harry_users'
PRODUCTS_TABLE = 'harry_products'

@stage4_bp.route('/', methods=["GET"])
def login_page():
    if 'name' in session.keys():
        return redirect('index')
    return render_template(f"stage4/login.html")

@stage4_bp.route('/login', methods=["POST"])
def login():
    if 'name' in session.keys():
        return redirect('index')

    try:
        command_format = f"SELECT username FROM {USERS_TABLE} WHERE username=%(username)s AND password=%(password)s;"
        with create_cursor() as cursor:
            cursor.execute(command, {'password': request.json['password'], 'username': request.json['username']})
            row = cursor.fetchone()
            session['name'] = row[0]
            return redirect('index')
    
    except ProgrammingError as e:
        return e.msg

    except Exception as e:
        return "Inccorrect password"

@stage4_bp.route('/register', methods=["POST"])
def register():
    if 'name' in session.keys():
        return redirect('index')

    try:
        exists_command = f"SELECT username FROM {USERS_TABLE} WHERE username=%(username)s;"
        insert_command = f"INSERT INTO {USERS_TABLE} ('username', 'password') VALUES (%(username)s, %(password)s);"
        with create_cursor() as cursor:
            cursor.execute(exists_command, {'username': request.json['username']})
            if cursor.fetchone is not None:
                return "username already exists"
            
            cursor.execute(insert_command, {'password': request.json['password'], 'username': request.json['username']})
            return "Succesfully registered"
    
    except ProgrammingError as e:
        return e.msg

    except Exception as e:
        return "Internal error"

@stage4_bp.route('/delete_account', methods=['GET'])
def delete_account():
    if 'name' not in session.keys():
        return redirect('login')
    
    command = f"DELETE FROM {USERS_TABLE} where username='{session['name']}';"
    with create_cursor() as cursor:
        cursor.execute(command)
        return redirect('login')


@stage4_bp.route("/logout", methods=['GET'])
def logout():
    if 'name' in session.keys():
        session.clear()
    return redirect('.')

@stage4_bp.route("/index")
def index():
    if 'name' not in session.keys():
        return redirect('.')

    return render_template("stage4/index.html")

@stage4_bp.route("/search", methods=['POST'])
def search():
    if 'name' not in session.keys():
        return redirect("login")
    
    command = f"SELECT name, description, price, amount_in_stock FROM {PRODUCTS_TABLE}"
    params = dict()
    if 'search_string' in request.json.keys():
        command += ' WHERE name LIKE %(search_string)s'
        params['search_string'] = request.json['search_string']

    with create_cursor() as cursor:
        cursor.execute(command, params)
        return cursor.fetchall()