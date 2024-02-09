from flask import Flask, render_template, request
from sympy import symbols, diff, integrate, simplify, SympifyError

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
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
                return render_template('index.html', resultado=resultado, error=error)

            # Simplificar el resultado
            resultado = simplify(resultado)
            resultado = str(resultado)
        except SympifyError as e:
            error = f"Error al procesar la función: {e}"
        except Exception as e:
            error = f"Error inesperado: {e}"

    return render_template('index.html', resultado=resultado, error=error)

if __name__ == '__main__':
    app.run(debug=True)
