from flask import Flask, render_template
app = Flask(__name__)

# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def checkerboard_8_8():
    return render_template ("index.html", rows = 8, columns = 8, color1 = "#556B2F", color2= "#FFFFE0")# Put the default rows, columns and colors 

# /http://localhost:5000/x - should display 8 by x checkerboard
@app.route('/<rows>')
def checkerboard_x_8(rows):
    if (rows.isnumeric()):
        rows = int(rows)
        return render_template ("index.html", rows = rows, columns = 8, color1 = "#556B2F", color2= "#FFFFE0")# Put the default columns and colors 
    return "Error: please enter a valid number, try again !"

# /http://localhost:5000/x/y - should display y by x checkerboard
@app.route('/<rows>/<columns>')
def checkerboard_x_y(rows, columns):
    if (rows.isnumeric() and columns.isnumeric()):
        rows = int(rows)
        columns = int(columns)
        return render_template ("index.html", rows = rows, columns = columns, color1 = "#556B2F", color2= "#FFFFE0")# Put the default colors
    return "Error: please enter a valid number, try again !"

# /http://localhost:5000/x/y/color1/color2 - should display y by x checkerboard with selected color
@app.route('/<rows>/<columns>/<color1>/<color2>')
def checkerboard_x_y_with_color(rows, columns, color1, color2):
    if (rows.isnumeric() and columns.isnumeric()):
        rows = int(rows)
        columns = int(columns)
        return render_template ("index.html", rows = rows, columns = columns, color1 = color1, color2= color2)# Pass the entered values
    return "Error: please enter a valid number, try again !"

# Ensure this file is being run directly and not from a different module
if (__name__ == "__main__"):
    app.run(debug = True) # Run the app in debug mode