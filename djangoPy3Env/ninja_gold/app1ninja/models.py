from django.db import models

# Create your models here.
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