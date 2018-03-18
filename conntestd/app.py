from flask import Flask
from flask import g
from conntestd.config import SECRET_KEY
from conntestd.config import DB_CONN
from conntestd.db import get_db_session
from conntestd.db import init_db


app = Flask(__name__)
app.url_map.strict_slashes = False
app.secret_key = SECRET_KEY


@app.before_request
def pre_request():
    g.db = get_db_session(DB_CONN, True)


@app.after_request
def post_request(resp):
    try:
        g.db.close()
    except:
        pass
    return resp



if __name__ == "__main__":
    init_db(DB_CONN)
    app.run('0.0.0.0', threaded=True, debug=True)
