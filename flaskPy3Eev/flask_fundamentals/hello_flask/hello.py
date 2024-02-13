from flask import Flask  # Import Flask (class) to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app" {I think name to give it a unique name}

@app.route('/')          # The "@" decorator associates this route with the function immediately following {/ --> root}
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


# import statements, maybe some other routes
@app.route('/success')
def success():
    return "success"
# We can add a variable rules to our routes
@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

# We can add as many of these as we need, giving each variable a different name
@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

# app.run(debug=True) should be the very last statement!
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.