from flask import Flask, render_template
from blueprints.auth.views import bp as bp_auth

app = Flask(__name__)
app.secret_key = 'qwerty123'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

app.register_blueprint(bp_auth)
