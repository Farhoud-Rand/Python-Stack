from django.shortcuts import render, redirect
import sys
import random # import the random module

# This page used to select the game difficulty  
def welcome(request):
    if 'number' not in request.session :                    # Check if 'number' key exists in session
        request.session['number'] = random.randint(1, 100) 	# random number between 1-100
    if 'tries' not in request.session :                     # Check if 'tries' key exists in session
        request.session['tries'] = 0
    print(request.session['number'])
    print("*"*80)
    sys.stdout.flush() # To ensure that the print statements are immediately visible in the terminal while the Flask server is running, you can explicitly flush the output buffer after each print statement using sys.stdout.flush().
    return render(request,"welcome.html")

# Easy game
def easy(request):
    return render(request,"easy.html")

# Hard game
def hard(request):
    if 'winners' not in request.session:
        request.session['winners'] = []
    if 'limit' not in request.session :                     # Check if 'limit' key exists in session
        request.session['limit'] = 5
        request.session['type'] = 'hard'
    print(request.session)
    print("*"*80)
    sys.stdout.flush() # To ensure that the print statements are immediately visible in the terminal while the Flask server is running, you can explicitly flush the output buffer after each print statement using sys.stdout.flush().
    return render(request,"hard.html",{'limit':request.session['limit']})

def check_number(request):
    if (request.method == 'POST'):
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
            return render(request,"limit_fail.html",context) # Fail case (hard game)
    if (request.session['user_number'] == request.session['number']):  # Case 1: Success (easy game)
        return render(request,"success.html",context)
    else:
        return render(request,"fail.html",context)            # Fail case (easy game)
    
# Clear the session 
def clear_session(request):
    # Store the winner list to keep it
    item_to_keep = request.session.get('winners', None)
    # Clear all data from the session
    request.session.clear()
    # Set the retained item back into the session
    if item_to_keep is not None:
        request.session['winners'] = item_to_keep
    return redirect("/")

# Leaderbord 
def leaderbord(request):
    if (request.method == 'POST'):
        winners = request.session['winners']
        name = request.POST['winner_name']
        print(name)
        print("*"*80)
        sys.stdout.flush()
        if (name not in request.session['winners']):
            print("ADD new one")
            sys.stdout.flush()
            win_record = {'name':name,'tries':request.session['tries']}
            
            winners.append(win_record)
            request.session['winners'] = winners
            # session['winners'] += (win_record)
            print ("NEW LIST :")
            print(request.session['winners'])
            sys.stdout.flush()
        else: 
            print("Update if need")
            sys.stdout.flush()
            if request.session['winners'][name] > request.session['tries']:
                request.session['winners'][name] =  request.session['tries']
            print ("Updated LIST :")
            print(request.session['winners'])
            sys.stdout.flush()
        return redirect("/show_leaderboard" )
    
# Show Leaderbord 
def show_leaderbord(request):
    # Sort the winners list based on the number of tries
    winners = request.session['winners']
    winners.sort(key=lambda x: x['tries'])
    return render(request,"leaderboard.html", {'winners' : winners})

# Go back to home
def back_home(request):
    del request.session['limit']
    del request.session['number']
    del request.session['tries']
    return redirect('/')



    





