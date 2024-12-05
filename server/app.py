import argparse
from flask import Flask, render_template, redirect, request, session
from flask_session import Session
import logging

from .consts import DEFAULT_PORT, DEFAULT_HOST, PROJECT_ROOT
from .utils.mysql import create_cursor
from .utils.general import get_file_contents

from .blueprints.management import management_bp
from .blueprints.stage1 import stage1_bp
from .blueprints.stage2 import stage2_bp
from .blueprints.stage3 import stage3_bp
from .blueprints.stage4 import stage4_bp

# Disable flask logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(management_bp)
app.register_blueprint(stage1_bp, url_prefix="/stage1")
app.register_blueprint(stage2_bp, url_prefix="/stage2")
app.register_blueprint(stage3_bp, url_prefix="/stage3")
app.register_blueprint(stage4_bp, url_prefix="/stage4")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", dest="host", default=DEFAULT_HOST, type=str)
    parser.add_argument("--port", dest="port", default=DEFAULT_PORT, type=int)

    return parser.parse_args()


def main():
    args = parse_args()
    app.run(host=args.host, port=args.port, debug=True)


if "__main__" == __name__:
    main()