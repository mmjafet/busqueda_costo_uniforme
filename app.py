from flask import Flask
from flask import render_template
from costo_uniforme import busca_costo_uniforme, Nodo, mapa_carreteras

app = Flask(__name__)

@app.route("/")
def index():
    # Lógica para obtener el resultado de costo_uniforme
    nodo_inicial = Nodo('Edo. Méx.')
    solucion = 'Hidalgo'

    resultado = busca_costo_uniforme(nodo_inicial, solucion, mapa_carreteras)

    if resultado is not None:
        costo, nodo_solucion = resultado
        mensaje = f'El camino más corto desde {nodo_inicial.get_datos()} a {nodo_solucion.get_datos()} tiene un costo de {costo}.'
    else:
        mensaje = 'No se encontró ninguna solución.'

    return render_template("index.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)
