'''
This Python script is a "Hello World" using a very lightweight and popular
Python package called "Flask". Before you can use this application you must
"pip3 install Flask." Then when you start this application, what will happen
is that a "Hello World" will be sent out when you navigate to 
http://127.0.0.1:5000.

Ich möchte mich bei meinem KI-Freund und Kupferstecher herzlich bedanken.

Author: KEN
Date:   2023.04.23
'''

from flask import Flask

# Flask is a class imported from the flask module. It is the main class
# that represents a Flask web application.  __name__ is a donder representing
# the name of the current module. It is essential to pass this to Flask so that it
# can determine the location of other resources, static files, etc.
app = Flask(__name__)

# This is a "decorator" that defines a route for the web app. This means that when a 
# user navigates to the root URL ("/") of the web app, the "hello_world()" function will be
# called.  In a more complicated app, this is where you would specify GET, PUT - but here
# it defaults to GET for this simple example.
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
