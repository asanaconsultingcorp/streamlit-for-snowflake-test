import os
import snowflake.connector

conn = snowflake.connector.connect(
    account='knondbh-naa00611',
    user='asanaconsultingcorp',
    password='Zpzp0809!abcde',
    #password=os.environ['SNOWSQL_PWD'],
    database='tests',
    schema='public',
    role='ACCOUNTADMIN',
    warehouse='COMPUTE_WH'
)

cur = conn.cursor()
cur.execute('select * from tests.public.employees')
for row in cur:
    print(row)

#df = cur.fetch_pandas_all();
#print(df)
