"""
B208 Advanced Algorithms - Pathfinding Project
Author: Kerem Altun
City: Potsdam
"""

import math
from models import potsdam_map

scenarios = [
    ('Museum_Barberini', 'Ernst_von_Bergmann_Hospital'),
    ('Brandenburger_Tor_Potsdam', 'St_Josefs_Hospital'),
    ('Park_Babelsberg', 'Oberlinklinik_Hospital'),
    ('Einstein_Tower', 'Ernst_von_Bergmann_Hospital'),
    ('New_Palace', 'EvB_West_Hospital')
]

coords = {
    'Museum_Barberini': (52.3955, 13.0622),
    'Ernst_von_Bergmann_Hospital': (52.4011, 13.0683),
    'Brandenburger_Tor_Potsdam': (52.3995, 13.0480),
    'St_Josefs_Hospital': (52.4005, 13.0398),
    'Park_Babelsberg': (52.4070, 13.0905),
    'Oberlinklinik_Hospital': (52.3915, 13.0950),
    'Einstein_Tower': (52.3800, 13.0645),
    'New_Palace': (52.4012, 13.0158),
    'EvB_West_Hospital': (52.3985, 13.0102)
}

def calculate_heuristic(node1, node2, coordinates):
    if node1 not in coordinates or node2 not in coordinates:
        return 0

    lat1, lon1 = coordinates [node1]
    lat2, lon2 = coordinates [node2]

    R= 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2 
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c
    
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
                h = calculate_heuristic(node, goal, coordinates) 
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
    d_res, d_nodes = dijkstra(potsdam_map, start, target)
    a_res, a_nodes = a_star(potsdam_map, start, target, coords)
    print(f"Scenario: {start} to {target}")
    print(f"  Dijkstra Result: {d_res:.2f} km {d_nodes}")
    print(f"  A* Result:       {a_res:.2f} km {a_nodes}")
    print("-" * 60)
