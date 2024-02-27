from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # Save data from form in the session and convert numbers to integers
    session['strawberry'] = int(request.form['strawberry'])
    session['raspberry'] = int(request.form['raspberry'])
    session['apple'] = int(request.form['apple'])
    session['blackberry'] = int(request.form['blackberry'])
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    return redirect('/result') # Redirecte the post request !

@app.route('/result')
def result():
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    