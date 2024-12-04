from flask import Flask, render_template, redirect, request, session, url_for
from flask_session import Session
import logging

from .consts import SERVER_PORT, SERVER_HOST
from .utils import create_cursor

# Disable flask logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h>Add stage number in url (e.g. /1)'

@app.route('/1', methods=["GET"])
def stage1():
    return render_template(f"stage1.html")

@app.route('/stage1', methods=["POST"])
def stage1_internal():
    logged_in_user = None
    try:
        command_format = "SELECT username FROM users1 WHERE username='{username}' AND password='{password}';"
        command = command_format.format(username=request.json['username'], password=request.json['password'])
        with create_cursor() as cursor:
            cursor.execute(command)
            row = cursor.fetchone()
            logged_in_user = row[0]
        
    except (IndexError, TypeError):
        pass
    
    if logged_in_user is None:
        return "Failed"
    return redirect(url_for("stage1_completed"))
    
@app.route("/stage1_completed")
def stage1_completed():
    return render_template("stage1_completed.html")


def main():
    app.run(host=SERVER_HOST, port=SERVER_PORT)

if "__main__" == __name__:
    main()