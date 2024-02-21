from flask import Flask 
app = Flask(__name__)

# Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def say_hello():
    return "Hello world!"

# Create a route that responds with "Dojo!
@app.route('/dojo')
def say_dojo():
    return "Dojo!"

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<name>')
def say_hi(name):
    return "Hi " + name.capitalize() + "!"

# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    if (number.isnumeric()):#  ensure the 2nd element in the URL is an integer
        number = int(number)
        return (word +"\n") * number
    return "Please enter a vaild number !! Make sure to write the URL as: /repeat/number/word"

# Ensure that if the user types in any route other than the ones specified, they receive an error message
@app.route('/<anyThing>')
def print_error(anyThing):
    return "Sorry! No response. Try again"

# Ensure this file is being run directly and not from a different module
if (__name__ == '__main__'):
    app.run(debug=True) # Run the app in debug mode