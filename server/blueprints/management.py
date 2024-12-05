from flask import Blueprint
from ..utils.mysql import create_cursor
from ..utils.general import get_file_contents
from ..consts import PROJECT_ROOT


management_bp = Blueprint("management", __name__)

@management_bp.route('/')
def hello():
    return '<a href="/stage1">go to stage 1</a>'

@management_bp.route('/resetDB')
def reset_database():
    # with create_cursor() as cursor:
    #    import pdb; pdb.set_trace()
    #    pass
    try:
        with create_cursor(database=None) as cursor:
            sql_dump = get_file_contents(PROJECT_ROOT / "schema.sql")
            cursor.execute(sql_dump)
            return "Reset done"
    except Exception as e:
        import pdb; pdb.set_trace
        return e.msg