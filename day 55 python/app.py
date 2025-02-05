#NUMBER GUESSING GAME 
# flask application for number guessing game.

from flask import Flask  # Import Flask class
import random

random_number = random.randint(0,9)
print(random_number)

# Create a Flask app instance
app = Flask(__name__)

#decorators
def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return f"<b>{result}</b>"
    wrapper.__name__ = func.__name__ 
    return wrapper

@app.route('/')
@bold
def home():
    return """
    Enter your guess from 0 to 9:<br>
    <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Funny GIF'/>
    """


@app.route('/<int:guess>')
@bold
def check_guess(guess):
    if guess > random_number:
        return f"<h1 style = 'color: red'>Your guess is too high.</h1>"  "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    
    
    elif guess < random_number:
        return f"<h1 style = 'color: red'>Your guess is too low. </h1>" "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return f"<h1 style = 'color: green'>You guessed right. </h1>" "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"    
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
