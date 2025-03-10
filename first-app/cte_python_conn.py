import _utils_python_conn as utils
conn = utils.getConnection()

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

cur = conn.cursor()
cur.execute(query)
for row in cur:
    print(row)