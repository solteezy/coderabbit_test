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

