# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return 'Aplicacion para potenciar ,Multiplicaciones '
#
# @app.route('/about')
# def about():
#     return 'About'


from flask import Flask, request, render_template
from sympy import *


val1 = Symbol('x')





#Se calcula la derivada de la funcion cos(sin(x^3)) con respecto a x


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vals = request.form.getlist('misvalores')
        # val1 = float(vals[0])
        # val2 = float(vals[1])
        val1 = Symbol('x')
        # val2 = Symbol('x')
        # val2 = float(vals[1])

        result = diff(val1)
    else:
        val1 = ''
        val2 = ''
        result = ''
    return render_template('index.html', val1=val1, val2=val2, result=result)
