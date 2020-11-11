import sqlite3

def show_color(username):
    #we connect to the db
    connection = sqlite3.connect('flask_tut.db',check_same_thread=False)

    #cursor
    cursor = connection.cursor()

    cursor.execute(

    """select favorite_color from users where username == '{username}' order by pk desc;""".format(username = username)

    )

    color = cursor.fetchone()[0]
    connection.commit()
    cursor.close()
    connection.close()

    message = '{username}s favorite color is {color}.'.format(username = username, color = color)

    return message

#check the password if its available in the db
def checkpwd(username):
    connection = sqlite3.connect('flask_tut.db',check_same_thread=False)

    cursor = connection.cursor()
    cursor.execute(
    """select password from users where username = '{username}' order by pk desc;""".format(username = username)
    )

    password = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return password

#check user
def check_users():
    connection = sqlite3.connect('flask_tut.db',check_same_thread=False)

    cursor = connection.cursor()
    cursor.execute(
    """select  username from users order by pk desc;"""
    )

    db_users = cursor.fetchall()

    users = []

    #loop through the db db_users
    for i in range (len(db_users)):
        person = db_users[i][0]
        users.append(person)

    connection.commit()
    cursor.close()
    connection.close()

    return users


#this the function that adds people to the database.
def signup(username, password, favorite_color):
    connection = sqlite3.connect('flask_tut.db',check_same_thread=False)

    cursor = connection.cursor()
    #check if the user is there.
    cursor.execute(
    """select password from users where username = '{username}' order by pk desc;""".format(username = username)
    )
    exist = cursor.fetchone()

    if exist is None:
        cursor.execute(
        """insert into users (username,password, favorite_color) values('{username}','password','favorite_color');""".format(username=username,password=password,favorite_color=favorite_color)
        )
    else:
        return("User Already Existed!")

    connection.commit()
    cursor.close()
    connection.close()
    #the return of the real function
    return 'You have successfully signed up'
