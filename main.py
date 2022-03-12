from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile', methods = ['GET','POST'])
def profile():
    username = request.forms['username']
    password = request.forms['password']
    return render_template('profile.html', username= username, password= password)

if __name__ == '__main__':
    app.run(debug= True)
    
