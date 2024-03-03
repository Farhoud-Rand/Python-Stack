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
    form = request.form['form'] # Get the form to select the min and max values
    min = 0
    max = 0
    if (form == 'farm'):
        min = 10
        max = 20
    elif (form == 'cave'):
        min = 5
        max = 10
    elif (form == 'house'):
        min = 2
        max = 5
    elif (form == 'casino'):
        min = -50
        max = 50
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
    return redirect("/") # Redirect the root route 

if __name__ == "__main__":
    app.run(debug=True)