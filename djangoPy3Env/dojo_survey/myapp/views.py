from django.shortcuts import render

# Root route
def index(request):
    return render(request,"index.html")

# Result route
def create_user(request):
     if request.method == "POST":
        # Check if the agreement is ticked
        if 'agree' not in request.POST:
            agree_from_form = "not agree"
        else: 
            agree_from_form = request.POST['agree']

        context = {
            'name':request.POST['name'], 
            'agreement':agree_from_form,
            'location':request.POST['location'],
            'language':request.POST['language'],
            'comment':request.POST['comment'],
            'gender':request.POST['gender'],
        }
        return render(request,"show.html", context)