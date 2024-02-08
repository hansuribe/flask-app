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


x = Symbol('x')





#Se calcula la derivada de la funcion cos(sin(x^3)) con respecto a x



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        vals = request.form.getlist('misvalores')
        # val1 = float(vals[0])
        # val2 = float(vals[1])
        val3 = (vals[0])
        a = diff(val3)
        result = a
    else:
        # val1 = ''
        # val2 = ''
        val3 = ""
        result = ''
    # return render_template('index.html', val1=val1, val2=val2, result=result)
        return render_template('index.html', val3=val3, result=result)
