from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola esta es mi primera app en vercel Exitos'

@app.route('/about')
def about():
    return 'About'
