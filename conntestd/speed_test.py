import datetime
import logging
import sys
from speedtest import Speedtest
from conntestd.db import get_db_session
from conntestd.db import SpeedTestResult
from conntestd.config import DB_CONN


logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                    level=logging.INFO,
                    stream=sys.stdout)


def run_speedtest():
    logging.info("Starting periodic connection test job.")
    db = get_db_session(DB_CONN)
    db_result = SpeedTestResult(dt=datetime.datetime.now(),
                                status='running')
    db.add(db_result)
    db.commit()

    try:
        s = Speedtest()
        s.get_best_server()
        s.download()
        s.upload()
        result = s.results.dict()
        download = result['download']
        upload = result['upload']
        ping = result['ping']
        country = result['server']['country']
        town = result['server']['name']
        sponsor = result['server']['sponsor']

        db_result.status = 'complete'
        db_result.download = download
        db_result.upload = upload
        db_result.ping = ping
        db_result.country = country
        db_result.town = town
        db_result.sponsor = sponsor
        db.commit()
        logging.info("Periodic connection test job completed.")

    except Exception as err:
        logging.error("Error occured during periodic connection test job: %s" % str(err))
        db_result.status = 'error'
        db.commit()

    finally:
        db.close()
