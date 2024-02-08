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
from sympy import symbols, diff, simplify


x = Symbol('x')





#Se calcula la derivada de la funcion cos(sin(x^3)) con respecto a x



app = Flask(__name__)

#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#
#
#         vals = request.form.getlist('misvalores')
#         val3 = float(vals['x'])
#         # val2 = float(vals[1])
#         # val3 = Symbol(vals[0])
#
#         a =  diff(val3)
#
#
#         result = a
#     else:
#         # val1 = ''
#         # val2 = ''
#         val3 = ""
#         result = ''
#     # return render_template('index.html', val1=val1, val2=val2, result=result)
#         return render_template('index.html',  result=result)


@app.route('/derivar', methods=['POST'])
def derivar():
    # Obtener la función ingresada por el usuario desde el formulario
    funcion = request.form['funcion']

    # Crear el símbolo para la variable independiente
    x = symbols('x')

    try:
        # Derivar la función ingresada utilizando SymPy
        funcion_derivada = diff(funcion, x)
        # Simplificar la derivada
        funcion_derivada = simplify(funcion_derivada)
        resultado = str(funcion_derivada)
    except Exception as e:
        resultado = f"No se pudo derivar la función: {e}"

    return render_template('index.html', resultado=resultado)
