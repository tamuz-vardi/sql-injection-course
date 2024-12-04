from flask import Flask, render_template, redirect, request, session, url_for, Blueprint
from flask_session import Session
from mysql.connector.errors import ProgrammingError
import logging

from ..consts import DEFAULT_PORT, DEFAULT_HOST, PROJECT_ROOT
from ..utils.mysql import create_cursor
from ..utils.general import get_file_contents

stage1_bp = Blueprint("stage1", __name__)


@stage1_bp.route('/', methods=["GET"])
def login_page():
    return render_template(f"stage1/login.html")

@stage1_bp.route('/login', methods=["POST"])
def login():
    try:
        command_format = "SELECT username FROM users1 WHERE username='{username}' AND password='{password}';"
        command = command_format.format(username=request.json['username'], password=request.json['password'])
        with create_cursor() as cursor:
            cursor.execute(command)
            row = cursor.fetchone()
            logged_in_user = row[0]
            return redirect('completion')
        
    except ProgrammingError as e:
        return e.msg
    except Exception:
        return "Incorrect password"
    
@stage1_bp.route("/completion")
def completion():
    return render_template("stage1/completion.html")
