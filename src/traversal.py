from graph import *
import queue as q


def breadth_first_search(graph, start=0):

    queue = q.Queue()
    queue.put(start)

    explored = np.zeros(graph.num_vertices)

    while not queue.empty():
        vertex = queue.get()

        if explored[vertex] == 1:
            continue

        print("Visited: ", vertex)

        explored[vertex] = 1

        for neighbour in graph.get_adjacent_vertices(vertex):
            if explored[neighbour] != 1:
                queue.put(neighbour)


def depth_first_search(graph, explored, current=0):

    if explored[current] == 1:
        return

    explored[current] = 1

    print("Visited: ", current)

    for child in graph.get_adjacent_vertices(current):
        depth_first_search(graph, explored, child)


# this is an undirected graph
g = AdjacencyMatrixGraph(9)

# add the edges to the graph
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

print("Breadth First Traversal")
# perform breadth first search starting from node 2 on the graph
breadth_first_search(g, 2)

print("Depth First Traversal")
is_visited = np.zeros(g.num_vertices)
# perform depth first search starting from node 2 on the graph
depth_first_search(g, is_visited, 2)
