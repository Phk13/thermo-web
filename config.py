

DB = {
    'host': '',
    'port': 27017,
    'user': 'thermo',
    'pass': '',
    'name': 'thermo',
    'collection': "reading"
}

DATABASE_URI = f"mongodb://{DB['user']}:{DB['pass']}@{DB['host']}:{DB['port']}/?authSource={DB['name']}"
SENSOR_URI = ''

SENSOR_INTERVAL = 2000
