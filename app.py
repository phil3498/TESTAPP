
from flask import Flask, render_template,  request, flash, url_for


app= Flask(__name__)  
app.secret_key = "al_20m "
# app.secret_key = 'd152c34b61fcf69d03c2eb689fc4f48b1fb03b121e93bd2643cc51447a59a0a2'


@app.route('/')
def index():
    flash(" what's your name ? ")
    return render_template("index.html")

@app.route('/greet', methods=["POST", "GET"])
def greet():    
    flash("Hi " + str(request.form['name_input']) +", great to see you ! ")
    return render_template("index.html")

    
if __name__ =='__main__':
    app.run(debug=True)  