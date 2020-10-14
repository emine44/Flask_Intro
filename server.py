"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html><html>Hi! This is the home page.<br>
    <a href ="http://localhost:5000/hello">Please click to go to Hello page</a>
    <a href ="http://localhost:5000/diss">Please click to go to Diss page</a>
     </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          What compliment would you like?
          <input type="radio" name="compliment" value="awesome">Awesome<br>
          <input type="radio" name="compliment" value="terrific">Terrific<br>
          <input type="radio" name="compliment" value="fantastic">Fantastic<br>
          <input type="radio" name="compliment" value="neato">Neato<br>
          <input type="radio" name="compliment" value="fantabulous">Fantabulous<br>
          <input type="radio" name="compliment" value="wowza">Wowza<br>
          <input type="radio" name="compliment" value="oh-so-not-meh">Oh-so-not-meh<br>
          <input type="radio" name="compliment" value="brilliant">Brilliant<br>
          <input type="radio" name="compliment" value="ducky">Ducky<br>
          <input type="radio" name="compliment" value="coolio">Coolio<br>
          <input type="radio" name="compliment" value="incredible">Incredible<br>
          <input type="radio" name="compliment" value="wonderful">Wonderful<br>
          <input type="radio" name="compliment" value="smashing">Smashing<br>
          <input type="radio" name="compliment" value="lovely">Lovely<br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def offer_greeting():
    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
    <head>
      <title>A Compliment</title>
    </head>
    <body>
      Hi {player} I think you're {compliment}!
    </body>
    </html>
    """

@app.route('/diss')
def say_hello_diss():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet_diss" method='GET'>
          What's your name? <input type="text" name="person">
          What diss would you like?
          <input type="radio" name="diss" value="mean">Mean<br>
          <input type="radio" name="diss" value="unkind">Unkind<br>
          <input type="radio" name="diss" value="fantastic">Fantastic<br>
          <input type="radio" name="diss" value="cruel">Cruel<br>
          <input type="radio" name="diss" value="horrible">Horrible<br>
          <input type="radio" name="diss" value="heartless">Heartless<br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/greet_diss')
def offer_greeting_diss():
    player = request.args.get("person")
    diss = request.args.get("diss")

return f"""
    <!doctype html>
    <html>
    <head>
      <title>A Compliment</title>
    </head>
    <body>
      Hi {player} I think you're {diss}!
    </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
