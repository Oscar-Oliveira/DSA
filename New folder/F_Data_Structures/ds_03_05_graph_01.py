"""
graph transversal - example
"""

from B_Data_Structures.queue_built_in import Queue_built_in_list
from B_Data_Structures.stack import Stack

def breadth_first(graph, start, f=None):
    queue = Queue_built_in_list()
    queue.insert(start)
    visited = []
    while not queue.is_empty():
        vertex = queue.remove()
        if vertex not in visited:
            visited.append(vertex)
            if f and f(vertex):
                return visited
            for v in graph.get(vertex):
                queue.insert(v)
    return visited

def depth_first_search(graph, start, f=None):
    stack = Stack()
    stack.push(start)
    visited = []
    while not stack.is_empty():
        vertex = stack.pop()
        if not vertex in visited:
            visited.append(vertex)
            if f and f(vertex):
                return visited
            for v in graph.get(vertex):
                stack.push(v)
    return visited

def main():

    graph = {}
    graph["A"] = ["B", "C", "D"]
    graph["B"] = ["E"]
    graph["C"] = ["F", "E"]
    graph["D"] = ["G", "H"]
    graph["E"] = []
    graph["F"] = []
    graph["G"] = []
    graph["H"] = []

    print(breadth_first(graph, "A"))
    print(breadth_first(graph, "A", lambda x: x == "D"))

    print()
    print(depth_first_search(graph, "A"))
    print(depth_first_search(graph, "A", lambda x: x == "D"))

if __name__ == "__main__":
    main()
    print("Done!!")
