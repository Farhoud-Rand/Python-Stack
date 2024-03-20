from django.shortcuts import render, redirect
from . import models

# Root route will show the index.html page 
def index(request):
    models.initialize_session(request)
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
        models.choose_random_number(request)
        models.format_date_time(request)
        models.write_output_string(request)
        models.check_target(request)
        return redirect("/") # Redirect the root route 

# Clear the session 
def clear_session(request):
    request.session.clear()  # clears all keys
    return redirect("/")