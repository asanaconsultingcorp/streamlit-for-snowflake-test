import _utils_snowpark as utils
session = utils.getSession()

query = """
with q1 as (
    SELECT DEPARTMENT, floor(AVG(SALARY)) AS AVERAGE_SALARY
    FROM EMPLOYEES
    GROUP BY DEPARTMENT
    order by department
)
SELECT e.department, e.employee_name, e.salary,
    (e.salary + (0.1 * q1.AVERAGE_SALARY)) as new_salary
from employees e
    join q1 on q1.department = e.department
where e.job = 'MANAGER'
order by e.department, e.employee_name
"""

df = session.sql(query)
rows= df.collect()
for row in rows:
    print(row)
    
df2 = session.sql(query).to_pandas()
print(df2)