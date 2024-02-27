from flask import Flask, render_template, request, redirect # Added request
app = Flask(__name__)
# Our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    # Check if the name is empty
    # If it empty display an alart to inform the user that the name cannot be empty
    # The window.history.back() function is called to navigate the user back to the previous page (the form page) after dismissing the alert.
    if name_from_form == '':
         return """
        <script>
            alert("Name cannot be empty!");
            window.history.back();
        </script>
        """
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']

    return render_template("show.html", name_on_template = name_from_form, location_on_template = location_from_form, language_on_template = language_from_form, comment_on_template = comment_from_form)

if __name__ == "__main__":
    app.run(debug=True)