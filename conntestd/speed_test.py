from speedtest import Speedtest
from conntestd.db import get_db_session
from conntestd.config import DB_CONN


def run_speedtest():
    try:
        s = Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        print(s.results)
    except Exception as err:
        print(str(err))
