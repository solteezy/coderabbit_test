

SQL_CREATE_TABLE = """
CREATE TABLE employees (
    id VARCHAR(255),
    name VARCHAR(10),
    age VARCHAR(10),
    salary VARCHAR(10),
    department VARCHAR(10)
);"""

SQL_SELECT_ALL = """SELECT * FROM employees;"""

SQL_SELECT_EMPLOYEE_BY_ID = """SELECT * FROM employees WHERE id = 1234;"""

SQL_SELECT_PRODUCT = """SELECT * FROM products WHERE product_id IN (SELECT product_id FROM orders);"""

SQL_SELECT_EMPLOYEE_BY_DEPARTMENT = """SELECT name, (SELECT department_name FROM departments WHERE departments.id = employees.department_id) FROM employees;"""

SQL_SELECT_DISTINCT_DEPARTMENTS = """SELECT DISTINCT department FROM departments;"""



def doStuff(x):
 for i in range(0, len(x)):
  if x[i]%2==0:
   print(str(x[i])+" is even")
  else:print(str(x[i])+" is odd")


def find_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

import sqlite3

def get_user_data(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()


def divide(a, b):
    return a / b


def is_adult(age):
    if age > 18:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(doStuff([1, 2, 3, 4, 5]))
    print(find_max([1, 2, 3, 4, 5]))
    print(get_user_data("John"))
    print(divide(10, 2))
    print(is_adult(20))

