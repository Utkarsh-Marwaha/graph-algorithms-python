import priority_dict as pq
from graph import *


def build_distance_table(graph, source):

    # A dictionary mapping the vertex ID to a tuple
    # of (distance from source, last vertex on path from source)
    distance_table = {}

    for v_id in range(graph.num_vertices):
        distance_table[v_id] = (None, None)

    distance_table[source] = (0, source)

    # Holds the mapping of vertex ID to distance from source vertex
    # Access the highest priority (lowest distance) item first
    priority_queue = pq.priority_dict()

    priority_queue[source] = 0

    while len(priority_queue.keys()) > 0:

        current_vertex = priority_queue.pop_smallest()

        # distance of the closest vertex from the source
        current_dist = distance_table[current_vertex][0]

        for neighbour in graph.get_adjacent_vertices(current_vertex):
            distance = current_dist + g.get_edge_weight(current_vertex, neighbour)

            # The last recorded distance to this neighbour from the source
            neighbour_distance = distance_table[neighbour][0]

            # If there is a currently recorded distance from the source and this
            # is greater than the distance of the new path found, update the current
            # distance of the neighbour from the source in the distance table
            if neighbour_distance is None or neighbour_distance > distance:
                distance_table[neighbour] = (distance, current_vertex)

                # also update the priority queue entry
                priority_queue[neighbour] = distance

    return distance_table


def shortest_path(graph, source, destination):

    distance_table = build_distance_table(graph, source)

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
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 6)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 5)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(0, 7, 8)

shortest_path(g, 0, 6)
shortest_path(g, 4, 7)
shortest_path(g, 7, 0)
