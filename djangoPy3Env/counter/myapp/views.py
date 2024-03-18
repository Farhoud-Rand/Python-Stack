from django.shortcuts import render, redirect

# Root route will handle rendering our refeashing the page
def index(request):
    # Check if 'actual_visits' key exists in session
    if 'actual_visits' not in request.session and 'visits' not in request.session:
        request.session['actual_visits'] = 1 # Inintialize the value to be 1
        request.session['visits'] = 1
    else:
        # Increment 'actual_visits' if it exists
        request.session['actual_visits'] += 1
        request.session['visits'] += 1
    context = {
        'actual_visits':request.session['actual_visits'],
        'visits':request.session['visits'],
    }
    return render(request,"index.html", context)

# Add two visits
def add2(request):
    request.session['visits'] += 2 # Increment 'visits' by 2
    return redirect("/counter")

# Reset visits
def reset(request):
    request.session['visits'] = 1 # Make the value to be 1
    return redirect("/counter")

# Clear the session 
def clear_session(request):
    request.session.clear() # clears all keys
    return redirect("/")

# Increment the number of visits by spcific number
def increment_by(request):
    if request.method == 'POST':
        if (request.POST['increment_by_number'] != ''):
            number = int(request.POST['increment_by_number']) # Convert the number to integer first
        else:
            number = 0
        request.session['visits'] += number # Add the number
        return redirect("/counter")

# Redirect route for all routes that increment the counter not the actual number of visits
def display_page(request):
    context = {
        'actual_visits':request.session['actual_visits'],
        'visits':request.session['visits'],
    }
    return render(request,"index.html",context)