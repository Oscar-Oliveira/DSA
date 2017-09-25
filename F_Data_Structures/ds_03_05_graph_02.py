"""
Dijkstra’s Algorithm
- See: https://www.youtube.com/watch?v=GazC3A4OQTE
"""

INFINITY = float("inf")

def lowest_distance_not_visited(distances, visited):
    lowest_distance = INFINITY
    lowest_distance_node = None
    for node in distances:
        cost = distances[node]
        if cost < lowest_distance and node not in visited:
            lowest_distance = cost
            lowest_distance_node = node
    return lowest_distance_node

def dijkstras_shortest_path(graph, start):
    previous = {}
    distances = {}
    for k in graph.keys():
        previous[k] = None
        distances[k] = INFINITY
    distances[start] = 0
    visited = []
    current_node = lowest_distance_not_visited(distances, visited)
    while current_node is not None:
        distance = distances[current_node]
        connections = graph[current_node]
        for k, distance in connections.items():
            new_distance = distance + distance
            if new_distance < distances[k]:
                distances[k] = new_distance
                previous[k] = current_node
        visited.append(current_node)
        current_node = lowest_distance_not_visited(distances, visited)
    return (distances, previous)

def main():

    graph = {
        "A": {"B":6, "D":1},
        "B": {"A":6, "D":2, "E":2, "C":5},
        "C": {"B":5, "E":5},
        "D": {"A":1, "E":1, "B":2},
        "E": {"D":1, "B":2, "C":5}, }

    """
    A -- 6 -- B -- 5
    |       / |     \
    1    2    2      C
    | /       |     /
    D -- 1 -- E -- 5
    """

    distances, previous = dijkstras_shortest_path(graph, "A")

    data = zip(sorted(distances.items()), sorted(previous.items()))
    s = "{:^10} | {:^10} | {:^10}"
    print(s.format("vertex", "shortest", "previous"))
    print(s.format("", "distance", "vertex"))
    print(s.format("-" * 10, "-" * 10, "-" * 10))
    for line in data:
        (a, b), (_, d) = (e_, _) = line
        print(s.format(str(a), str(b), str(d)))

if __name__ == "__main__":
    main()
    print("Done!!")
