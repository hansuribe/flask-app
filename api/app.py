from flask import Flask, render_template, request
from sympy import symbols, diff, integrate, simplify, SympifyError

import random

preguntas_respuestas = []


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
# Ruta para la tabla de multiplicar
@app.route('/tabla_multiplicar', methods=['GET', 'POST'])
def tabla_multiplicar():
    if not preguntas_respuestas:
        # Generar preguntas y respuestas si la lista está vacía
        for numero in range(2, 10):
            for multiplicador in range(2, 10):
                pregunta = f"{numero} x {multiplicador} = ?"
                respuesta_correcta = numero * multiplicador
                preguntas_respuestas.append((pregunta, respuesta_correcta))

    mensaje = None

    if request.method == 'POST':
        respuesta_usuario = int(request.form['respuesta'])
        pregunta, respuesta_correcta = preguntas_respuestas.pop(0)
        if respuesta_usuario == respuesta_correcta:
            mensaje = "¡Respuesta correcta!"
        else:
            mensaje = "Respuesta incorrecta. Inténtalo de nuevo."
            preguntas_respuestas.append((pregunta, respuesta_correcta))
            return redirect(url_for('tabla_multiplicar'))

    pregunta, _ = preguntas_respuestas[0]
    return render_template('tabla_multiplicar.html', pregunta=pregunta, mensaje=mensaje)


if __name__ == '__main__':
    app.run(debug=True)
