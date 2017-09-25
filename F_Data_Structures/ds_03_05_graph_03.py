"""
Bellman-Ford Algorithm
- See: https://www.youtube.com/watch?v=obWXjtg0L64
- See: https://www.programiz.com/dsa/bellman-ford-algorithm
"""

INFINITY = float("inf")

def bellman_ford_shortest_path(graph, start):
    previous = {}
    distances = {}
    for neighbour in graph.keys():
        previous[neighbour] = None
        distances[neighbour] = INFINITY
    distances[start] = 0
    for _ in range(len(graph)-1): #Run this until is converges
        for current_node in graph.keys():
            for neighbour, distance in graph[current_node].items():
                if distances[neighbour] > distances[current_node] + distance:
                    distances[neighbour] = distances[current_node] + distance
                    previous[neighbour] = current_node
    # Check for negative weight cycle
    for current_node in graph.keys():
        for neighbour, _ in graph[current_node].items():
            if distances[neighbour] > (distances[current_node] + graph[current_node][neighbour]):
                return None, None
    return (distances, previous)

def main():

    graph = {
        "A": {"B":5, "C":10},
        "B": {"D":3},
        "C": {"E":1},
        "D": {"E":6},
        "E": {"B":-7}
    }

    """
        5 -> B -- 3 -> D
      /        <       |
    A            -7    6
      \             \  >
       10 -> C -- 1 -> E
    """

    distances, previous = bellman_ford_shortest_path(graph, "A")

    if distances and previous:
        data = zip(sorted(distances.items()), sorted(previous.items()))
        s = "{:^10} | {:^10} | {:^10}"
        print(s.format("vertex", "shortest", "previous"))
        print(s.format("", "distance", "vertex"))
        print(s.format("-" * 10, "-" * 10, "-" * 10))
        for line in data:
            (a, b), (_, d) = (e_, _) = line
            print(s.format(str(a), str(b), str(d)))
    else:
        print("Negative weight cycle were found")

if __name__ == "__main__":
    main()
    print("Done!!")
