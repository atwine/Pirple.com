import sqlite3

connection = sqlite3.connect('flask_tut.db',check_same_thread = False)

cursor = connection.cursor()

cursor.execute(

    """insert into users(

    username,
    password,
    favorite_color

    ) values (
            'Gordon',
            'Ramsy',
            'Red'
    );"""

)

cursor.execute(

    """insert into users(

    username,
    password,
    favorite_color

    ) values (
            'Ironman',
            'Tonny',
            'Gold'
    );"""

)

connection.commit()
cursor.close()
connection.close()
