# Config postgreSQL Database
# "postgres://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
database_user = config['DEFAULT']['DB_USER']
database_password = config['DEFAULT']['DB_PASSWORD']
database_name = config['DEFAULT']['DB_NAME']
database_host = config['DEFAULT']['DB_HOST']

DATABASE_URI = f'postgresql://{database_user}:{database_password}@{database_host}/'
