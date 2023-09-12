# Create a simple Flask Application

from flask import Flask, render_template, request, url_for, redirect, jsonify

# Create flask app
app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# Index Route
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return f"This person has passed with {score}"

@app.route('/fail/<int:score>')
def fail(score):
    return f"This person has failed with {score}"

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == "GET":
        return render_template('form.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        
        average_marks = (maths + science + history) / 3
        res = ""
        
        if average_marks >= 50:
            res = "Success"
        else:
            res = "Fail"
        
        # Redirect to the 'success' or 'fail' route with the calculated score
        #return redirect(url_for(res, score=average_marks))
        return render_template('form.html', marks=average_marks)

if __name__ == "__main__":
    app.run(debug=True)
