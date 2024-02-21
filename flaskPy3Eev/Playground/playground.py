from flask import Flask, render_template
app = Flask(__name__)

# Additional page to say hello in the root route 
@app.route('/')
def hello_page():
    return render_template ("hello.html")

# /play route render a template with 3 blue boxes
@app.route('/play')
def play():
    return render_template ("index.html", number_of_boxes = 3, color = "#9FC5F8")# Put the default values for number of boxes and color

# /play/<x> route render a template with x number of blue boxes
@app.route('/play/<number>')
def play_with_number(number):
    if (number.isnumeric()): # Check if the number is valid
        number = int(number) # convert the string to number
        return render_template ("index.html", number_of_boxes = number, color = "#9FC5F8")# Pass the number of boxes that entered by the user in URL
    return "Error: please enter a valid number of boxes, try again !"

# /play/<x>/<color> route render a template with x number of boxes the color of the provided value
@app.route('/play/<number>/<color>')
def play_with_color(number, color):
    if (number.isnumeric()): # Check if the number is valid
        number = int(number) # convert the string to number
        return render_template ("index.html", number_of_boxes = number, color = color)# Pass the number of boxes and color entered by the user in URL
    return "Error: please enter a valid number of boxes, try again !"

# Ensure this file is being run directly and not from a different module
if (__name__ == "__main__"):
    app.run(debug = True) # Run the app in debug mode