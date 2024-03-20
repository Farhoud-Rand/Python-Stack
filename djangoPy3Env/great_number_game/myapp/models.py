from django.db import models
import sys
import random # import the random module

# Function to intialize session  
def initialize_session(request):
    if 'number' not in request.session :                        # Check if 'number' key exists in session
            request.session['number'] = random.randint(1, 100) 	# random number between 1-100
    if 'tries' not in request.session :                         # Check if 'tries' key exists in session
            request.session['tries'] = 0
    print(request.session['number'])
    print("*"*80)
    sys.stdout.flush() # To ensure that the print statements are immediately visible in the terminal while the server is running, you can explicitly flush the output buffer after each print statement using sys.stdout.flush().
#________________________________________________________________________________________________________
def initialize_session_hard_game(request):
    if 'winners' not in request.session:
        request.session['winners'] = []
    if 'limit' not in request.session :                     # Check if 'limit' key exists in session
        request.session['limit'] = 5
        request.session['type'] = 'hard'
    print(request.session)
    print("*"*80)
    sys.stdout.flush() # To ensure that the print statements are immediately visible in the terminal while the server is running, you can explicitly flush the output buffer after each print statement using sys.stdout.flush().
#________________________________________________________________________________________________________
# Function to check the user input, and according to it select the output string 
def check_user_input(request):
    # Check the limitation counter for hard game
    if 'limit' in request.session :
        if (request.session['limit'] > 0):
            request.session['limit'] -= 1
    request.session['tries'] += 1                                                         # Increment the number of visits by spcific number
    request.session['user_number'] = int(request.POST['user_number'])                     # Convert the number to integer first
    if (request.session['number']- 10 <= request.session['user_number'] < request.session['number'] ):    # Case 2: too close but lower than number by 10 or less
        request.session['result'] = 'Low'
    elif (request.session['number']  < request.session['user_number'] <= request.session['number'] + 10): # Case 3: too close but higher than number by 10 or less
        request.session['result'] = 'High'
    elif (request.session['user_number'] > request.session['number']):                            # Case 4: too far from number from above 
        request.session['result'] = 'Too high !'
    else:                                                                         # Case 5: too far from number from below
        request.session['result'] = 'Too low !'
#________________________________________________________________________________________________________
# Function to clear all data on session except winners list 
def clear_without_removeing_winner_list(request):
    # Store the winner list to keep it
    item_to_keep = request.session.get('winners', None)
    # Clear all data from the session
    request.session.clear()
    # Set the retained item back into the session
    if item_to_keep is not None:
        request.session['winners'] = item_to_keep
#________________________________________________________________________________________________________
# Function to add new winner to winners list
def add_update_winner_information(request):
    winners = request.session['winners']
    name = request.POST['winner_name']
    # Add new winner to the winners list
    if (name not in request.session['winners']):
        win_record = {'name':name,'tries':request.session['tries']}
        winners.append(win_record)
        request.session['winners'] = winners
#________________________________________________________________________________________________________
# Function to sort the winners list based on the number of tries
def sort_winners(request):
    winners = request.session['winners']
    winners.sort(key=lambda x: x['tries'])
    request.session['winners'] = winners
#________________________________________________________________________________________________________
# Function to remove current game information in order to start new game
def start_new_game(request):
    del request.session['limit']
    del request.session['number']
    del request.session['tries']