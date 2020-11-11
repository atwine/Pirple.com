import sqlite3

connection = sqlite3.connect('flask_tut.db',check_same_thread = False)
cursor = connection.cursor()

#creat table
cursor.execute(

    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(16),
        password VARCHAR(32),
        favorite_color VARCHAR(32)
        );"""

)
connection.commit()
cursor.close()
connection.close()

# sqlite> select * from users;
# 1|Gordon|Ramsy|Red
# 2|Ironman|Tonny|Gold
