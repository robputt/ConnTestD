import uuid
from os.path import expanduser

SECRET_KEY = str(uuid.uuid4())
HOME = expanduser('~')
DB_CONN = 'sqlite:////%s/.conntestd.db' % HOME
