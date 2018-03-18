import uuid
from os.path import expanduser

TEST_INTERVAL = 600
SECRET_KEY = str(uuid.uuid4())
HOME = expanduser('~')
DB_CONN = 'sqlite:////%s/.conntestd.db' % HOME
