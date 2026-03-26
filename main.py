"""
B208 Advanced Algorithms - Pathfinding Project
Author: Kerem Altun
City: Potsdam
"""

from models import potsdam_map

scenarios = [
    ('Museum_Barberini', 'Ernst_von_Bergmann_Hospital'),
    ('Brandenburger_Tor_Potsdam', 'St_Josefs_Hospital'),
    ('Park_Babelsberg', 'Oberlinklinik_Hospital'),
    ('Einstein_Tower', 'Ernst_von_Bergmann_Hospital'),
    ('New_Palace', 'EvB_West_Hospital')
]

coords = {}

# Dijkstra
def dijkstra(graph, start, goal):
    distances = {node: 9999 for node in graph}
    distances[start] = 0
    visited = []

    while len(visited) < len(graph):
        current_node = None
        min_dist = 10000
        for node in graph:
            if node not in visited and distances[node] < min_dist:
                min_dist = distances[node]
                current_node = node
        
        if current_node is None or current_node == goal:
            break
            
        visited.append(current_node)

        for neighbor, weight in graph[current_node].items():
            new_path = distances[current_node] + weight
            if new_path < distances[neighbor]:
                distances[neighbor] = new_path
                
    return distances[goal], len(visited)

# A*
def a_star(graph, start, goal, coordinates):
    distances = {node: 9999 for node in graph}
    distances[start] = 0
    visited = []

    while len(visited) < len(graph):
        current_node = None
        min_f_score = 10000
        
        for node in graph:
            if node not in visited:
                h = 0.2 
                f_score = distances[node] + h
                
                if f_score < min_f_score:
                    min_f_score = f_score
                    current_node = node
        
        if current_node is None or current_node == goal:
            break
            
        visited.append(current_node)

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
                
    return distances[goal], len(visited)

# Evaluation
print("POTSDAM EMERGENCY PATHFINDING TEST RESULTS\n")
for start, target in scenarios:
    d_res = dijkstra(potsdam_map, start, target)
    a_res = a_star(potsdam_map, start, target, coords)
    print(f"Scenario: {start} to {target}")
    print(f"  Dijkstra Result: {d_res} km")
    print(f"  A* Result:       {a_res} km")
    print("-" * 30)
