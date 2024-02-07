from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Aplicacion de Multiplicaciones'

@app.route('/about')
def about():
    return 'About'
