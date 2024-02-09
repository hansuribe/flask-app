from flask import Flask, render_template, request
from sympy import symbols, diff, integrate, simplify, SympifyError

import random


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

# Nueva ruta para la tabla de multiplicar
@app.route('/tabla_multiplicar', methods=['GET', 'POST'])
def tabla_multiplicar():
    pregunta = None
    respuesta_correcta = None
    respuesta_usuario = None
    mensaje = None

    if request.method == 'POST':
        respuesta_usuario = int(request.form['respuesta'])
        if respuesta_usuario == respuesta_correcta:
            mensaje = "¡Respuesta correcta!"
        else:
            mensaje = "Respuesta incorrecta. Inténtalo de nuevo."

    else:
        # Generar aleatoriamente la pregunta de la tabla de multiplicar
        numero = random.randint(2, 9)
        multiplicador = random.randint(2, 9)
        pregunta = f"{numero} x {multiplicador} = ?"
        respuesta_correcta = numero * multiplicador

    return render_template('tabla_multiplicar.html', pregunta=pregunta, mensaje=mensaje)







if __name__ == '__main__':
    app.run(debug=True)
