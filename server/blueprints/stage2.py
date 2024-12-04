from flask import Flask, render_template, redirect, request, session, url_for, Blueprint
from flask_session import Session
from mysql.connector.errors import ProgrammingError
import logging

from ..consts import DEFAULT_PORT, DEFAULT_HOST, PROJECT_ROOT
from ..utils.mysql import create_cursor
from ..utils.general import get_file_contents

stage2_bp = Blueprint("stage2", __name__)


@stage2_bp.route('/', methods=["GET"])
def login_page():
    return render_template(f"stage2/login.html")

@stage2_bp.route('/login', methods=["POST"])
def login():
    try:
        command_format = "SELECT username FROM users1 WHERE username=%(username)s AND password='{password}';"
        command = command_format.format(password=request.json['password'])
        with create_cursor() as cursor:
            cursor.execute(command, {'username': request.json['username']})
            row = cursor.fetchone()
            logged_in_user = row[0]
            return redirect('completion')
    
    # except ProgrammingError as e:
    #     return e.msg
    except Exception:
        return "Incorrect password"
    
@stage2_bp.route("/completion")
def completion():
    return render_template("stage2/completion.html")
