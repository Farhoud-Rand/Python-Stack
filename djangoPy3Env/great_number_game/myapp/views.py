from django.shortcuts import render, redirect
from . import models

# This page used to select the game difficulty  
def welcome(request):
    models.initialize_session(request)
    return render(request,"welcome.html")

# Easy game
def easy(request):
    return render(request,"easy.html")

# Hard game
def hard(request):
    models.initialize_session_hard_game(request)
    return render(request,"hard.html",{'limit':request.session['limit']})

def check_number(request):
    if (request.method == 'POST'):
        models.check_user_input(request)
        return redirect('/show_result')
           
# show result (because if I use render-template in check-number function it will decrease the numbers when we refresh the page)
def show(request):
    context = {
        'tries' : request.session['tries'],
        'number': request.session['number']
    }
    if ('limit' in request.session and request.session['limit'] == 0): # Check if last attempt was correct (hard game)
        if (request.session['user_number'] == request.session['number']):
            return render(request,"success.html",context)
        else:
            return render(request,"limit_fail.html",context)           # Fail case (hard game)
    if (request.session['user_number'] == request.session['number']):  # Case 1: Success (easy game)
        return render(request,"success.html",context)
    else:
        return render(request,"fail.html",context)                     # Fail case (easy game)
    
# Clear the session 
def clear_session(request):
    models.clear_without_removeing_winner_list(request)
    return redirect("/")

# Leaderbord page
def leaderbord(request):
    if (request.method == 'POST'):
        models.add_update_winner_information(request)
        return redirect("/show_leaderboard" )
    
# Show Leaderbord 
def show_leaderbord(request):
    models.sort_winners(request)
    return render(request,"leaderboard.html", {'winners' : request.session['winners']})

# Go back to home
def back_home(request):
    models.start_new_game(request)
    return redirect('/')