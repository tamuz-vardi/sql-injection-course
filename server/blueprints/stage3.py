from flask import Flask, render_template, redirect, request, session, url_for, Blueprint, session
from flask_session import Session
import logging

from mysql.connector.errors import ProgrammingError

from ..consts import DEFAULT_PORT, DEFAULT_HOST, PROJECT_ROOT
from ..utils.mysql import create_cursor
from ..utils.general import get_file_contents

stage3_bp = Blueprint("stage3", __name__)


@stage3_bp.route('/', methods=["GET"])
def login_page():
    if 'name' in session.keys():
        return redirect('index')
    return render_template(f"stage3/login.html")

@stage3_bp.route('/login', methods=["POST"])
def login():
    if 'name' in session.keys():
        return redirect('index')

    try:
        command_format = "SELECT username, is_admin FROM users1 WHERE (username='{username}' AND password=%(password)s);"
        command = command_format.format(username=request.json['username'])
        with create_cursor() as cursor:
            cursor.execute(command, {'password': request.json['password']})
            row = cursor.fetchone()
            (session['name'], session['is_admin']) = row
            return redirect('index')
    
    except ProgrammingError as e:
        return e.msg

    except Exception as e:
        return "Inccorrect password"

@stage3_bp.route("/logout", methods=['GET'])
def logout():
    if 'name' in session.keys():
        session.clear()
    return redirect('.')

@stage3_bp.route("/index")
def index():
    if 'name' not in session.keys():
        return redirect('.')

    return render_template("stage3/index.html")

@stage3_bp.route("/admin")
def admin_page():
    if 'is_admin' in session.keys() and session['is_admin'] == 1:
        return render_template("stage3/completion.html")
    else:
        return redirect('index')
