from flask import Flask, render_template, redirect, url_for, request,redirect, g,session
#call the model script you made before.
import model

app = Flask(__name__)

#we need a secret KEY
app.secret_key = 'jumpjacks'

username = ''
user = model.check_users()#this is going to be a function in model.py

#what happens before before_request
@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username'] #this calls an empty session as per username which is empty

#in the route below: "/" means the home pages
@app.route('/',methods = ['GET']) #this is like how you see : www.google.com
def home():
    if 'username' in session:
        g.user = session['username'] #g is the global variable for flask

        return render_template('football.html', message = '<img src = static/avatar.jpeg>')

    return render_template('homepage.html', message = 'Login to the page or signup!')


#login functionality of the app.
@app.route('/login', methods = ['GET','POST']) #we use post because we are going to use a form.
def login():
    if request.method == 'POST':
        session.pop('username', None) #first you clear the session that there could be before loggin in.
        areyouuser = request.form.get('username') #pick the username from the form.
        pwd = model.checkpwd(areyouuser) #check the password of the username
        if request.form.get('password') == pwd:
            session['username'] = request.form.get('username')
            return redirect(url_for('home')) #if the password is correct then take them home.
    return render_template('index.html')#if not then take them to the index.html page.

    """#we need an if statment there
    if request.method =='GET':
        return render_template('index.html')
    else:
        #we have to build something in the index pages
        #this is how we pick the information from the text fields in the webpage
        #its better to use request.form.get : it helps you avoid badrequest errors
        username = request.form.get('username')
        password = request.form.get('password')
        db_password = model.checkpwd(username)
        #
        if  password == db_password:
            #one of the things you can do is to take the person to another page after logging in.
            #in the code below I have taken the person to the profile page after logging in.
            message = model.show_color(username)
            return render_template('index.html', message = message)
        else:
            error = 'Hint, Atwine --> Birthday'
            return render_template('index.html', message = error)"""

#create another route
#seems like routes are the same as pages
@app.route('/football', methods = ['GET'])
def football():
    return   render_template('football.html')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = 'Please Sign Up!'
        return   render_template('signup.html', message = message)
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        favorite_color = request.form.get('favorite_color')
        return render_template('signup.html', message = model.signup(username, password, favorite_color))

#here I want to create another route for about so that I can add information there about us
@app.route('/about',methods = ['GET'])
def about():
    return render_template('about.html')

#this takes you to the already logged in session of the application.
@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

#logout of the application.
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('home'))


if __name__ == '__main__': #this helps you run the app
    app.run(port = 7000, debug = True)
    #when you declare debug = True when you make changes you don't have to keep terminating the server.
