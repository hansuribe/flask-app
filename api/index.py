from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Aplicacion para potenciar ,Multiplicaciones '

@app.route('/about')
def about():
    return 'About'
