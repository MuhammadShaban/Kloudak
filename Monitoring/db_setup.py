#/usr/bin/python3.6

from sqlalchemy import create_engine
from config import get_config
from orm_schema import base, Area, Pool, Host, VirtualMachine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

conf_dict = get_config('conf.json')
postgres_db = {'drivername': 'postgres',
               'username': 'mon_admin',
               'password': 'Maglab123!',
               'host': conf_dict['database'],
               'port': 5432,
               'database': 'monitor'}
uri = URL(**postgres_db)
engine = create_engine(uri)
base.metadata.create_all(engine)
print('created schema')