from django.shortcuts import render, redirect
import random
import sys
from datetime import datetime
from . import models

# Root route will show the index.html page 
def index(request):
    # Define the keys in the session
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

    context = {
        'total_golds':request.session['total_golds'],
        'activities':request.session['activities'],
        'show_alert':request.session['show_alert'],
        'message':request.session['message'],
        'result':request.session['result']
    }
    return render(request,"index.html", context)


# This route called when we submit any form, it will:
# * choose a random number (according to the submitted form)
# * Calculte the total number of golds
# * Add the new activity 
# * redirect the root route 
def process_money(request):
    if request.method == 'POST':
        print(request.POST)
        form = request.POST['form']     # Get the form to add it in the activity
        min = int(request.POST['min'])  # Get the min value
        max = int(request.POST['max'])  # Get the max value

        random_number = random.randint(min, max) # Choose a random number
        print("_"*100)
        print(random_number)
        print("_"*100)
        sys.stdout.flush()
        request.session['total_golds'] += random_number # Calculate the total number of golds
    
        # Get current date and time
        current_datetime = datetime.now()
        # Format the time as hours:minutes AM/PM and date as year-month-day
        formatted_time = current_datetime.strftime("%Y-%m-%d %I:%M %p")
        if (random_number > 0):
            output = f"Earned {random_number} golds from the {form}! ({formatted_time})"
        else:
            output = f"Entered a casino and lost {abs(random_number)} golds... Ouch.. ({formatted_time})" 
        request.session['activities'].insert(0,output) # Add the new activity (note use insert function instead of append in order to put the newest activity in the top)
        
        # Decrease the number of attempts
        request.session['attempts'] -= 1
        models.check_target(request)
    
        return redirect("/") # Redirect the root route 

# Clear the session 
def clear_session(request):
    # del request.session 
    request.session.clear()  # clears all keys
    return redirect("/")