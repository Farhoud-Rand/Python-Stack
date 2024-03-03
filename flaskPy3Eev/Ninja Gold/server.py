import random
import sys
from datetime import datetime
from flask import Flask, render_template, redirect, session, request, url_for

app = Flask(__name__)
app.secret_key = '123456789' # Add secret key for session 

# Root route will show the index.html page 
@app.route('/')
def index():
    # Define the keys in the session
    if 'total_golds' not in session:
        session['total_golds'] = 0 # This key will save the total number of golds the user have 
    if 'activities' not in session:
        session['activities'] = [] # This key will save the list of user submittion activities
    return render_template("index.html")

# This route called when we submit any form, it will:
# * choose a random number (according to the submitted form)
# * Calculte the total number of golds
# * Add the new activity 
# * redirect the root route 
@app.route('/process_money', methods=['post'])
def process_money():
    form = request.form['form']     # Get the form to add it in the activity
    min = int(request.form['min'])  # Get the min value
    max = int(request.form['max'])  # Get the max value

    random_number = random.randint(min, max) # Choose a random number
    print("_"*100)
    print(random_number)
    print("_"*100)
    sys.stdout.flush()
    session['total_golds'] += random_number # Calculte the total number of golds
    
    # Get current date and time
    current_datetime = datetime.now()
    # Format the time as hours:minutes AM/PM and date as year-month-day
    formatted_time = current_datetime.strftime("%Y-%m-%d %I:%M %p")
    if (random_number > 0):
        output = f"Earned {random_number} golds from the {form}! ({formatted_time})"
    else:
        output = f"Entered a casino and lost {abs(random_number)} golds... Ouch.. ({formatted_time})" 
    session['activities'].insert(0,output) # Add the new activity (note use insert function instead of append in order to put the newest activity in the top)
    return redirect(url_for("index"))      # Redirect the root route 

# Clear the session 
@app.route('/destroy_session')
def clear_session():
    session.clear() # clears all keys
    return redirect("/")

# Route to render the small window
@app.route('/small_window')
def small_window():
    return render_template('result.html')

# Route to handle closing the small window
@app.route('/close_small_window')
def close_small_window():
    # Redirect back to the main page
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)


