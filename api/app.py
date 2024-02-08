from flask import Flask, render_template, request
from sympy import symbols, diff, integrate, simplify, latex, SympifyError

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    resultado_tex = None
    error = None
    if request.method == 'POST':
        try:
            # Obtener la función ingresada por el usuario desde el formulario
            funcion = request.form['funcion']
            operacion = request.form['operacion']

            # Crear el símbolo para la variable independiente
            x = symbols('x')

            if operacion == 'derivada':
                # Derivar la función ingresada utilizando SymPy
                resultado = diff(funcion, x)
            elif operacion == 'integral':
                # Integrar la función ingresada utilizando SymPy
                resultado = integrate(funcion, x)
            else:
                error = "Operación no válida"
                return render_template('index.html', resultado=resultado, resultado_tex=resultado_tex, error=error)

            # Simplificar el resultado
            resultado = simplify(resultado)
            resultado_tex = latex(resultado)
        except SympifyError as e:
            error = f"Error al procesar la función: {e}"
        except Exception as e:
            error = f"Error inesperado: {e}"

    return render_template('index.html', resultado=resultado, resultado_tex=resultado_tex, error=error)
