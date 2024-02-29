from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "my_key"

# Our index route will handle rendering our form
@app.route('/')
def index():
    # Check if 'visits' key exists in session
    if 'visits' not in session:
        session['visits'] = 1 # Inintialize the value to be 1
    else:
        # Increment 'visits' if it exists
        session['visits'] += 1
    return render_template("index.html")

# Add two visits
@app.route('/add_two')
def add2():
    # Note: since I will redirect the root route so I will aready incremant visit by 1 
    # Check if 'visits' key exists in session
    if 'visits' not in session:
        session['visits'] = 1 # Inintialize the value to be 1
    else:
        # Increment 'visits' if it exists
        session['visits'] += 1
    return redirect("/")

# Add two visits
@app.route('/reset')
def reset():
    # Note: since I will redirect the root route so I will aready incremant visit by 1 
    session['visits'] = 0 # Inintialize the value to be 0
    return redirect("/")

# Clear the session 
@app.route('/destroy_session')
def clear_session():
    session.clear() # clears all keys
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)