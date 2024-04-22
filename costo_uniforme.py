from queue import PriorityQueue
from BFS import Nodo
def busca_costo_uniforme(nodo_inicial, solucion, mapa_carreteras):
    nodos_frontera = PriorityQueue()
    nodos_frontera.put((0, nodo_inicial))  # La cola con prioridad se ordena por el primer elemento de la tupla
    nodos_visitados = []

    while not nodos_frontera.empty():
        (costo, nodo_actual) = nodos_frontera.get()

        if nodo_actual.get_datos() == solucion:
            return (costo, nodo_actual)

        nodos_visitados.append(nodo_actual)

        for ciudad, costo_camino in mapa_carreteras[nodo_actual.get_datos()].items():
            nodo_hijo = Nodo(ciudad)

            if nodo_hijo not in nodos_visitados:
                nodos_frontera.put((costo + costo_camino, nodo_hijo))

    return None  # No se encontró ninguna solución

# El mapa de carreteras y los costos entre las ciudades
mapa_carreteras = {
    'Edo. Méx.': {'CDMX': 125, 'SLP': 513},
    'CDMX': {'Michoacán': 491, 'SLP': 423},
    'SLP': {'Sonora': 603, 'Monterrey': 313, 'Hidalgo': 599, 'Qro.': 203},
    'Michoacán': {'Sonora': 346, 'Monterrey': 309},
    'Qro.': {'Hidalgo': 390},
    'Monterrey': {'Sonora': 296, 'Qro.': 394},
    'Guadalajara': {},
    'Sonora': {},
    'Hidalgo': {},
    'Puebla': {}
}

nodo_inicial = Nodo('Edo. Méx.')
solucion = 'Hidalgo'

resultado = busca_costo_uniforme(nodo_inicial, solucion, mapa_carreteras)

if resultado is not None:
    (costo, nodo_solucion) = resultado
    print(f'El camino más corto desde {nodo_inicial.get_datos()} a {nodo_solucion.get_datos()} tiene un costo de {costo}.')
else:
    print('No se encontró ninguna solución.')