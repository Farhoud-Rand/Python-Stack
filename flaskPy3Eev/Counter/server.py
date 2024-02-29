from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "my_key"

# Our index route will handle rendering our refeashing the page
@app.route('/')
def index():
    # Check if 'actual_visits' key exists in session
    if 'actual_visits'  not in session and 'visits'  not in session:
        session['actual_visits'] = 1 # Inintialize the value to be 1
        session['visits'] = 1
    else:
        # Increment 'actual_visits' if it exists
        session['actual_visits'] += 1
        session['visits'] += 1
    return render_template("index.html")

# Add two visits
@app.route('/add_two')
def add2():
    session['visits'] += 2 # Increment 'visits' by 2
    return redirect("/counter")

# Reset visits
@app.route('/reset')
def reset():
    session['visits'] = 1 # Make the value to be 1
    return redirect("/counter")

# Clear the session 
@app.route('/destroy_session')
def clear_session():
    session.clear() # clears all keys
    return redirect("/")

# Increment the number of visits by spcific number
@app.route('/increment_by', methods=['POST'])
def increment_by():
    if (request.form['increment_by_number'] != ''):
        number = int(request.form['increment_by_number']) # Convert the number to integer first
    else:
        number = 0
    session['visits'] += number # Add the number
    return redirect("/counter")

# Redirect route for all routes that increment the counter not the actual number of visits
@app.route('/counter')
def display_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)