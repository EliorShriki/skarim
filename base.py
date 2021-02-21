from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from configparser import ConfigParser

import cx_Oracle

from os import environ
environ['NLS_LANG'] = ".AL32UTF8"

config_object = ConfigParser()
config_object.read(fr'config.ini')
dbinfo = config_object["db"]

MAX_IDENTIFIER_LENGTH = int(dbinfo["MAX_IDENTIFIER_LENGTH"])
ECHO = False if dbinfo["ECHO"].lower()=='false' else True if dbinfo["ECHO"].lower()=='true' else dbinfo["ECHO"]
ECHO_POOL = False if dbinfo["ECHO_POOL"].lower()=='false' else True if dbinfo["ECHO_POOL"].lower()=='true' else dbinfo["ECHO_POOL"]

dsn = cx_Oracle.makedsn(
    host = dbinfo["HOST"],
    port = dbinfo["PORT"],
    sid = dbinfo["SID"])

conn_str=f'{dbinfo["DIALECT"]}+{dbinfo["SQL_DRIVER"]}://{dbinfo["USERNAME"]}:{dbinfo["PASSWORD"]}@{dsn}'
engine = create_engine(conn_str, max_identifier_length = MAX_IDENTIFIER_LENGTH, echo = ECHO, echo_pool = ECHO_POOL)

# engine = create_engine(f'{dbinfo["DIALECT"]}+{dbinfo["SQL_DRIVER"]}://{dbinfo["USERNAME"]}:{dbinfo["PASSWORD"]}@{dbinfo["HOST"]}:{dbinfo["PORT"]}/?sid={dbinfo["SID"]}?'), max_identifier_length = MAX_IDENTIFIER_LENGTH, echo = ECHO, echo_pool = ECHO_POOL)
# engine = create_engine(f'{dbinfo["DIALECT"]}+{dbinfo["SQL_DRIVER"]}://{dbinfo["USERNAME"]}:{dbinfo["PASSWORD"]}@{dbinfo["HOST"]}:{dbinfo["PORT"]}/?service_name={dbinfo["SERVICE_NAME"]}?'), max_identifier_length = MAX_IDENTIFIER_LENGTH, echo = ECHO, echo_pool = ECHO_POOL)

Session = sessionmaker(bind=engine)

Base = declarative_base()