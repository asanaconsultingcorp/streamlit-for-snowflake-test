import os
import pandas as pd
from snowflake.snowpark import Session

pars =  {
    "account": 'knondbh-naa00611',
    "user": 'asanaconsultingcorp',
    #"password": 'Zpzp0809!abcde',
    "password": os.environ['SNOWSQL_PWD'],
    "database": 'tests',
    "schema": 'public',
    "role": 'ACCOUNTADMIN',
    "warehouse": 'COMPUTE_WH'
}

session = Session.builder.configs(pars).create()

df = session.sql('select * from employees')
rows= df.collect()
for row in rows:
    print(row)
    
    
#dfp = df.to_pandas()
#print(dfp)