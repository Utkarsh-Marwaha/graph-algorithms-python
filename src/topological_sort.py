import queue as q
from graph import *


def topological_sort(graph):
    queue = q.Queue()

    in_degree_map = {}

    for vertex in range(graph.num_vertices):
        in_degree_map[vertex] = graph.get_in_degree(vertex)

        # queues all nodes which have no dependencies i.e. no incoming edges
        if in_degree_map[vertex] == 0:
            queue.put(vertex)

    top_sort_result = []

    while not queue.empty():

        next_vertex = queue.get()
        top_sort_result.append(next_vertex)

        for dependent_vertex in graph.get_adjacent_vertices(next_vertex):
            in_degree_map[dependent_vertex] -= 1

            if in_degree_map[dependent_vertex] == 0:
                queue.put(dependent_vertex)

    if len(top_sort_result) != graph.num_vertices:
        raise ValueError("This graph has a cycle")

    return top_sort_result


# this is an undirected graph
directed_acyclic_graph = AdjacencyMatrixGraph(9, directed=True)

# add the edges to the graph
directed_acyclic_graph.add_edge(0, 1)
directed_acyclic_graph.add_edge(1, 2)
directed_acyclic_graph.add_edge(2, 7)
directed_acyclic_graph.add_edge(2, 4)
directed_acyclic_graph.add_edge(2, 3)
directed_acyclic_graph.add_edge(1, 5)
directed_acyclic_graph.add_edge(5, 6)
directed_acyclic_graph.add_edge(3, 6)
directed_acyclic_graph.add_edge(3, 4)
directed_acyclic_graph.add_edge(6, 8)

print(topological_sort(directed_acyclic_graph))
