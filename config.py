DEBUG = True

USERNAME = 'root'
PASSWORD = 'Daymongol16%'
SERVER = 'localhost'
DB = 'videos'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True


