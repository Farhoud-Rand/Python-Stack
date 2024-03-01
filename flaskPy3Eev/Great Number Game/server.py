import sys
import random # import the random module
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "my_key"

# Our index route will handle rendering our refeashing the page
@app.route('/')
def index():
    # Check if 'number' key exists in session
    if 'number' not in session :
        session['number'] = random.randint(1, 100) 	# random number between 1-100
    if 'tries' not in session :
        session['tries'] = 0
    print(session)
    print("*"*80)
    sys.stdout.flush() # To ensure that the print statements are immediately visible in the terminal while the Flask server is running, you can explicitly flush the output buffer after each print statement using sys.stdout.flush().
    return render_template("index.html")

# Increment the number of visits by spcific number
@app.route('/guess_from_user', methods=['POST'])
def check_number():
    session['tries'] += 1
    user_number = int(request.form['user_number']) # Convert the number to integer first
    if (user_number == session['number']):                             # Case 1: Success
        return render_template("success.html")
    elif (session['number']- 10 <= user_number < session['number'] ):  # Case 2: too close but lower than number by 10 or less
        session['result'] = 'Low'
    elif (session['number']  < user_number <= session['number'] + 10): # Case 3: too close but higher than number by 10 or less
        session['result'] = 'High'
    elif (user_number > session['number']):                            # Case 4: too far from number from above 
        session['result'] = 'Too high !'
    else:                                                              # Case 5: too far from number from below
        session['result'] = 'Too low !'
    return render_template("fail.html")        
        

# Clear the session 
@app.route('/destroy_session')
def clear_session():
    session.clear() # clears all keys
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)