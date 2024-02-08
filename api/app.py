from flask import Flask, render_template, request
from sympy import symbols, diff, simplify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
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
