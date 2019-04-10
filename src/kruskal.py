import priority_dict as pq
from graph import *


def has_cycle(spanning_tree):

    for source in spanning_tree:

        q = list()
        q.append(source)

        is_visited = set()
        while len(q) > 0:

            vertex = q.pop()

            # if we've seen the vertex before in this spanning tree
            # there is a cycle
            if vertex in is_visited:
                return True

            is_visited.add(vertex)

            # Add all vertices connected by edges in this spanning tree
            q.extend(spanning_tree[vertex])

    return False


def minimum_spanning_tree(graph):

    # Holds the mapping of vertex ID to distance from source vertex
    # Access the highest priority (lowest distance) item first
    priority_queue = pq.priority_dict()

    for v in range(graph.num_vertices):
        for neighbour in graph.get_adjacent_vertices(v):
            priority_queue[(v, neighbour)] = graph.get_edge_weight(v, neighbour)

    # Keeps track of all the visited nodes
    is_visited = set()

    spanning_tree = {}

    for v in range(graph.num_vertices):
        spanning_tree[v] = set()

    # number of edges added to the spanning tree
    num_edges = 0

    while len(priority_queue.keys()) > 0 and num_edges < graph.num_vertices - 1:

        # edge is represented by a pair of vertices
        v1, v2 = priority_queue.pop_smallest()

        if v1 in spanning_tree[v2]:
            continue

        # arrange the spanning tree so that the node with the smaller
        # vertex ID is always first. This greatly simplifies the code to
        # find cycles within the tree at each step
        vertex_pair = sorted([v1, v2])

        spanning_tree[vertex_pair[0]].add(vertex_pair[1])

        # check if adding the current edge creates a cycle within the spanning tree
        if has_cycle(spanning_tree):
            spanning_tree[vertex_pair[0]].remove(vertex_pair[1])
            continue
            
        num_edges += 1
        is_visited.add(v1)
        is_visited.add(v2)

    print("Visited Vertices: ", is_visited)

    if len(is_visited) != graph.num_vertices:
        print("Minimum Spanning Tree not found")
    else:
        print("Minimum Spanning Tree")
        for key in spanning_tree:
            for value in spanning_tree[key]:
                print(key, " --> ", value)


# this is an undirected unweighted graph
g = AdjacencyMatrixGraph(8, directed=False)

# add the edges to the graph
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 2)
g.add_edge(1, 4, 3)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 2)
g.add_edge(3, 6, 1)
g.add_edge(6, 7, 1)
g.add_edge(7, 0, 1)

minimum_spanning_tree(g)
