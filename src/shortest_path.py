import queue as q
from graph import *


def build_dist_table(graph, source):

    # A dictionary mapping the vertex ID to a tuple
    # of (distance from source, last vertex on path from source)
    distance_table = {}

    for v_id in range(graph.num_vertices):
        distance_table[v_id] = (None, None)

    # The distance from the source node to itself is 0
    distance_table[source] = (0, source)

    queue = q.Queue()
    queue.put(source)

    while not queue.empty():
        current_vertex = queue.get()

        # the distance of the current vertex from the source
        current_dist = distance_table[current_vertex][0]

        for neighbour in graph.get_adjacent_vertices(current_vertex):
            # Only update the distance table if no current distance from
            # the source is set
            if distance_table[neighbour][0] is None:
                distance_table[neighbour] = (current_dist + 1, current_vertex)

                # enqueue the neighbour only if it has other adjacent vertices to explore
                if len(graph.get_adjacent_vertices(neighbour)) > 0:
                    queue.put(neighbour)

    return distance_table


def shortest_path(graph, source, destination):

    distance_table = build_dist_table(graph, source)

    path = [destination]

    preceding_vertex = distance_table[destination][1]

    while preceding_vertex is not None and preceding_vertex is not source:

        path.insert(0, preceding_vertex)
        preceding_vertex = distance_table[preceding_vertex][1]

    if preceding_vertex is None:
        print("There is no path from %d to %d" % (source, destination))
    else:
        path.insert(0, source)
        print("Shortest Path is: ", path)


# this is an undirected unweighted graph
g = AdjacencyMatrixGraph(9, directed=False)

# add the edges to the graph
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)
g.add_edge(5, 4)
g.add_edge(3, 6)
g.add_edge(6, 6)
g.add_edge(0, 7)

shortest_path(g, 0, 5)
shortest_path(g, 0, 6)
shortest_path(g, 7, 4)
