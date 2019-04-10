import priority_dict as pq
from graph import *


def minimum_spanning_tree(graph, source):

    # A dictionary mapping the vertex ID to a tuple
    # of (distance from source, last vertex on path from source)
    distance_table = {}

    for v_id in range(graph.num_vertices):
        distance_table[v_id] = (None, None)

    # The distance from the source to itself is 0
    distance_table[source] = (0, source)

    # Holds the mapping of vertex ID to distance from source vertex
    # Access the highest priority (lowest distance) item first
    priority_queue = pq.priority_dict()

    priority_queue[source] = 0

    # Keeps track of all the visited nodes
    is_visited = set()

    # Set of edges where each edge is represented as a string
    # "1->2" is an edge between vertices 1 and 2
    spanning_tree = set()

    while len(priority_queue.keys()) > 0:
        current_vertex = priority_queue.pop_smallest()

        # if we've visited a vertex then we have all the outbound
        # edges from it, we do not process it again
        if current_vertex in is_visited:
            continue

        is_visited.add(current_vertex)

        # if the current vertex is the source, we haven't traversed an
        # edge yet, no edge to add to our spanning tree
        if current_vertex != source:

            # The current vertex is connected by the lowest weight edge
            last_vertex = distance_table[current_vertex][1]

            edge = str(last_vertex) + "-->" + str(current_vertex)

            if edge not in spanning_tree:
                spanning_tree.add(edge)

        for neighbour in graph.get_adjacent_vertices(current_vertex):

            # The distance to the neighbour is only the weight of the edge connecting to the neighbour
            distance = g.get_edge_weight(current_vertex, neighbour)

            # The last recorded distance to this neighbour from the source
            neighbour_distance = distance_table[neighbour][0]

            # If there is a currently recorded distance from the source and this
            # is greater than the distance of the new path found, update the current
            # distance of the neighbour from the source in the distance table
            if neighbour_distance is None or neighbour_distance > distance:

                distance_table[neighbour] = (distance, current_vertex)

                # also update the priority queue entry
                priority_queue[neighbour] = distance

    print("Minimum Spanning Tree with source node: ", source)
    for edge in spanning_tree:
        print(edge)


# this is an undirected unweighted graph
g = AdjacencyMatrixGraph(9, directed=False)

# add the edges to the graph
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 3)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)

minimum_spanning_tree(g, 1)
minimum_spanning_tree(g, 3)
