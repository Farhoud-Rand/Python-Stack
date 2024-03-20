import random
import sys
from datetime import datetime

# Function to define keys in the session
def initialize_session(request):
    if 'total_golds' not in request.session:
        request.session['total_golds'] = 0    # This key will save the total number of golds the user have 
    if 'activities' not in request.session:
        request.session['activities'] = []    # This key will save the list of user submittion activities
    if 'show_alert' not in request.session:
        request.session['show_alert'] = False # This key will save the list of user submittion activities
    if 'attempts' not in request.session:
        request.session['attempts'] = 10      # Number of attempts allowed
    if 'target_gold' not in request.session:
        request.session['target_gold'] = 100  # Target gold to reach
    if 'message' not in request.session:
        request.session['message'] = ''       # Message in alart
    if 'result' not in request.session:
        request.session['result'] = ''        # Type of alart
    if 'random_number' not in request.session:
        request.session['random_number'] = 0  # Random Number
    if 'formatted_date_time' not in request.session:
        request.session['formatted_date_time'] = '' 
#________________________________________________________________________________________________________________________________________
# Function to select random number in specific range 
def choose_random_number(request):    
    min = int(request.POST['min'])  # Get the min value
    max = int(request.POST['max'])  # Get the max value

    random_number = random.randint(min, max) # Choose a random number
    request.session['random_number'] = random_number
    print("_"*100)
    print(random_number)
    print("_"*100)
    sys.stdout.flush()
    request.session['total_golds'] += random_number # Calculate the total number of golds
#________________________________________________________________________________________________________________________________________
# Function to get and format date & time
def format_date_time(request):
    # Get current date and time
        current_datetime = datetime.now()
        # Format the time as hours:minutes AM/PM and date as year-month-day
        formatted_date_time = current_datetime.strftime("%Y-%m-%d %I:%M %p")
        request.session['formatted_date_time'] = formatted_date_time
#________________________________________________________________________________________________________________________________________
# Function to write the output string about the activity
def write_output_string(request):
    form = request.POST['form']     # Get the form to add it in the activity
    if (request.session['random_number'] > 0):
        output = f"Earned {request.session['random_number']} golds from the {form}! ({request.session['formatted_date_time']})"
    else:
        output = f"Entered a casino and lost {abs(request.session['random_number'])} golds... Ouch.. ({request.session['formatted_date_time']})" 
    request.session['activities'].insert(0,output) # Add the new activity (note use insert function instead of append in order to put the newest activity in the top)
    # Decrease the number of attempts
    request.session['attempts'] -= 1
#________________________________________________________________________________________________________________________________________    
# Function to check if the user get the targer number of golds or not
def check_target(request):
    # Check if the user reached the target gold
    if request.session['total_golds'] >= request.session['target_gold']:
        request.session['show_alert'] = True  # Set flag to show the alert
        request.session['message'] = "Congratulations! You have reached 100 gold!"
        request.session['result'] = 'success'
    elif request.session['attempts'] == 0 and request.session['total_golds'] < request.session['target_gold']:
        request.session['show_alert'] = True  # Set flag to show the alert
        request.session['message'] = "Oops! You have run out of attempts. Try again!"
        request.session['result'] = 'error'