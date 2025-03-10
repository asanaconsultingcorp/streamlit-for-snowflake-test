import os
from snowflake.snowpark import Session

def getSession():
    return Session.builder.configs({
        "account": 'knondbh-naa00611',
        "user": 'asanaconsultingcorp',
        #"password": 'Zpzp0809!abcde',
        "password": os.environ['SNOWSQL_PWD'],
        "database": 'tests',
        "schema": 'public',
        "role": 'ACCOUNTADMIN',
        "warehouse": 'COMPUTE_WH'
    }).create()