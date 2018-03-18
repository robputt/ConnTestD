from apscheduler.jobstores.memory import MemoryJobStore
from flask import Flask
from flask import g
from flask_apscheduler import APScheduler
from conntestd.config import SECRET_KEY
from conntestd.config import DB_CONN
from conntestd.config import TEST_INTERVAL
from conntestd.db import get_db_session
from conntestd.db import init_db
from conntestd.speed_test import run_speedtest
from conntestd.views import views_bp


class Config(object):
    JOBS = [
        {
            'id': 'periodic_speedtest',
            'func': run_speedtest,
            'trigger': 'interval',
            'seconds': TEST_INTERVAL
        }
    ]

    SCHEDULER_JOBSTORES = {
        'default': MemoryJobStore()
    }

    SCHEDULER_API_ENABLED = False


app = Flask(__name__)
app.config.from_object(Config())
app.url_map.strict_slashes = False
app.secret_key = SECRET_KEY
app.register_blueprint(views_bp)


@app.before_request
def pre_request():
    g.db = get_db_session(DB_CONN)


@app.after_request
def post_request(resp):
    try:
        g.db.close()
    except:
        pass
    return resp


def main():
    init_db(DB_CONN)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    run_speedtest()
    app.run('0.0.0.0', threaded=True)


if __name__ == "__main__":
    main()
