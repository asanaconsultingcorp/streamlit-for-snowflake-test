import os
import snowflake.connector

def getConnection():
    return snowflake.connector.connect(
        account='knondbh-naa00611',
        user='asanaconsultingcorp',
        password='Zpzp0809!abcde',
        #password=os.environ['SNOWSQL_PWD'],
        database='tests',
        schema='public',
        role='ACCOUNTADMIN',
        warehouse='COMPUTE_WH'
    )
    