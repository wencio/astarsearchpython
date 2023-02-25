import heapq

graph = {'S': {'A': 3, 'B': 4},
         'A': {'C': 4, 'D': 2},
         'B': {'D': 5, 'E': 2},
         'C': {'G': 5},
         'D': {'G': 7},
         'E': {'G': 3},
         'G': {}}


def a_star_search(graph, start, goal):
    # Creamos una cola de prioridad
    frontier = [(0, start)]
    # Creamos un diccionario para almacenar los nodos visitados y sus respectivos costos
    visited = {start: 0}
    # Creamos un diccionario para almacenar los nodos padre de cada nodo visitado
    parent = {}

    while frontier:
        # Obtenemos el nodo con la menor distancia estimada
        _, current = heapq.heappop(frontier)

        # Si llegamos al nodo de destino, retornamos la ruta construida
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path

        # Recorremos los vecinos del nodo actual
        for neighbor in graph[current]:
            # Calculamos la distancia estimada desde el nodo actual hasta el vecino
            cost = visited[current] + graph[current][neighbor] + heuristic(neighbor, goal)
            # Si el vecino no ha sido visitado, lo agregamos a la cola de prioridad
            if neighbor not in visited or cost < visited[neighbor]:
                visited[neighbor] = cost
                priority = cost
                heapq.heappush(frontier, (priority, neighbor))
                parent[neighbor] = current

    # Si no encontramos ninguna ruta, retornamos None
    return None

# Función heurística para estimar la distancia restante desde un nodo hasta el nodo de destino
def heuristic(n1, n2):
    return abs(n2[0] - n1[0]) + abs(n2[1] - n1[1])

# Ejemplo de uso
start = 'S'
goal = 'G'
path = a_star_search(graph, start, goal)
print(path)