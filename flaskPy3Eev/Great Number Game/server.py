import sys
import random # import the random module
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "my_key"

# This page used to select the game difficulty  
@app.route('/')
def welcome():
    if 'number' not in session :                    # Check if 'number' key exists in session
        session['number'] = random.randint(1, 100) 	# random number between 1-100
    if 'tries' not in session :                     # Check if 'tries' key exists in session
        session['tries'] = 0
    print(session)
    print("*"*80)
    sys.stdout.flush() # To ensure that the print statements are immediately visible in the terminal while the Flask server is running, you can explicitly flush the output buffer after each print statement using sys.stdout.flush().
    return render_template("welcome.html")

# Easy game
@app.route('/easy')
def easy():
    return render_template("easy.html")

# Hard game
@app.route('/hard')
def hard():
    if 'limit' not in session :                     # Check if 'limit' key exists in session
        session['limit'] = 5
        session['winners'] = [{'name':'rand','tries':4}]
    print(session)
    print("*"*80)
    sys.stdout.flush() # To ensure that the print statements are immediately visible in the terminal while the Flask server is running, you can explicitly flush the output buffer after each print statement using sys.stdout.flush().
    return render_template("hard.html")

@app.route('/guess_from_user', methods=['POST'])
def check_number():
    # Check the limitation counter for hard game
    if 'limit' in session :
        if (session['limit'] > 0):
            session['limit'] -= 1
    session['tries'] += 1                                                         # Increment the number of visits by spcific number
    session['user_number'] = int(request.form['user_number'])                     # Convert the number to integer first
    if (session['number']- 10 <= session['user_number'] < session['number'] ):    # Case 2: too close but lower than number by 10 or less
        session['result'] = 'Low'
    elif (session['number']  < session['user_number'] <= session['number'] + 10): # Case 3: too close but higher than number by 10 or less
        session['result'] = 'High'
    elif (session['user_number'] > session['number']):                            # Case 4: too far from number from above 
        session['result'] = 'Too high !'
    else:                                                                         # Case 5: too far from number from below
        session['result'] = 'Too low !'
    return redirect('/show_result')
           
# show result (because if I use render-template in check-number function it will decrease the numbers when we refresh the page)
@app.route('/show_result')
def show():
    if ('limit' in session and session['limit'] == 0): # Check if last attempt was correct (hard game)
        if (session['user_number'] == session['number']):
            return render_template("success.html")
        else:
            return render_template ("limit_fail.html") # Fail case (hard game)
    if (session['user_number'] == session['number']):  # Case 1: Success (easy game)
        return render_template("success.html")
    else:
        return render_template("fail.html")            # Fail case (easy game)
    
# Clear the session 
@app.route('/destroy_session')
def clear_session():
    session.clear() # clears all keys
    return redirect("/")

# Leaderbord 
@app.route('/leaderboard', methods=['post'])
def leaderbord():
    name = request.form['winner_name']
    print(name)
    print("*"*80)
    sys.stdout.flush()
    if (name not in session['winners']):
        print("ADD new one")
        sys.stdout.flush()
        win_record = {'name':name,'tries':session['tries']}
        session['winners'].append(win_record)
        print ("NEW LIST :")
        print(session['winners'])
        # sys.stdout.flush()
    else: 
        pass
        # print("Update if need")
        # sys.stdout.flush()
        # if session['winners'][name] > session['tries']:
        #     session['winners'][name] =  session['tries']
        # print ("Updated LIST :")
        # print(session['winners'])
        # sys.stdout.flush()
    return redirect("/show_leaderboard")
    
# Show Leaderbord 
@app.route('/show_leaderboard')
def show_leaderbord():
    return render_template("leaderboard.html")

if __name__ == "__main__":
    app.run(debug=True)