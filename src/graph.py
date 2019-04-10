import abc
import numpy as np


class Graph(abc.ABC):
    """
    The base class representation of a graph with all the
    interface methods.
    """
    def __init__(self, num_vertices, directed=False):
        """
        :param num_vertices: Total number of vertices present in the graph
        :param directed: True if the graph is directed, False otherwise
        """
        self.num_vertices = num_vertices
        self.directed = directed

    @abc.abstractmethod
    def add_edge(self, v1, v2, weight):
        """
        :param v1: vertex of the edge
        :param v2: vertex of the edge
        :param weight: weight of the edge connecting vertices v1 and v2
        :return:
        """
        pass

    @abc.abstractmethod
    def get_adjacent_vertices(self, v):
        """
        :param v: vertex whose adjacent vertices we want to retrieve
        :return: all the vertices adjacent to the given vertex
        """
        pass

    @abc.abstractmethod
    def get_in_degree(self, v):
        """

        :param v: vertex whose in-degree we wish to compute
        :return:  number of edges which are incident on the given vertex
        """
        pass

    @abc.abstractmethod
    def get_edge_weight(self, v1, v2):
        """

        :param v1: vertex of the edge whose weight we wish to retrieve
        :param v2: vertex of the edge whose weight we wish to retrieve
        :return: return the weight of the edge connecting vertex v1 and v2
        """
        pass

    @abc.abstractmethod
    def display(self):
        """
        This method displays the graph
        """
        pass


class AdjacencyMatrixGraph(Graph):
    """
    Represents a graph as an adjacency matrix. A cell in the matrix has
    a value when there exists an edge between the vertex represented by
    the row and column numbers.

    Weighted graphs can hold values > 1 in the matrix cells. A value of
    0 in the cell indicates that there is no edge
    """

    def __init__(self, num_vertices, directed=False):
        super(AdjacencyMatrixGraph, self).__init__(num_vertices, directed)

        self.matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, v1, v2, weight=1):

        # check if the vertices are valid
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        # check if the weight is positive
        if weight < 1:
            raise ValueError("An edge cannot have weight < 1")

        # assign the weight to the edge between the specified vertices
        self.matrix[v1][v2] = weight

        # in case the graph is undirected, we need an edge which goes in the opposite direction as well
        if not self.directed:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self, v):

        # check if the vertex is valid
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex %d is out of bounds" % v)

        adjacent_vertices = []

        for to_vertex in range(self.num_vertices):
            if self.matrix[v][to_vertex] > 0:
                adjacent_vertices.append(to_vertex)

        return adjacent_vertices

    def get_in_degree(self, v):

        # check if the vertex is valid
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex %d is out of bounds" % v)

        in_degree = 0

        for from_vertex in range(self.num_vertices):
            if self.matrix[from_vertex][v] > 0:
                in_degree += 1

        return in_degree

    def get_edge_weight(self, v1, v2):

        # check if the vertices are valid
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        return self.matrix[v1][v2]

    def display(self):
        for from_vertex in range(self.num_vertices):
            for to_vertex in self.get_adjacent_vertices(from_vertex):
                print(from_vertex, "-->", to_vertex)


g = AdjacencyMatrixGraph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)


for i in range(4):
    print("Adjacent to:", i, g.get_adjacent_vertices(i))

# display the in_degree for each vertex in the graph
for i in range(4):
    print("In degree: ", i, g.get_in_degree(i))

# display the weight for each edge in the graph
for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge weight: ", i, " ", j, "weight: ", g.get_edge_weight(i, j))

# display the graph
g.display()


class Node:
    """
    A single node in a graph represented by an adjacency set. Every node
    has a vertex id and is associated with a set of adjacent vertices
    """
    def __init__(self, vertex_id):
        """

        :param vertex_id: A unique number ranging from 0 to num_vertices - 1
        """
        self.vertex_id = vertex_id
        self.adjacency_set = set()

    def add_edge(self, v):

        # check if the vertex is valid
        if self.vertex_id == v:
            raise ValueError("Vertex %d cannot be adjacent to itself" % v)

        self.adjacency_set.add(v)

    def get_adjacency_set(self):
        return sorted(self.adjacency_set)


class AdjacencySetGraph(Graph):
    """
    Represents a graph as an adjacency set. A graph is a list of Nodes
    and each node has a set of adjacent vertices.

    This graph in its current form cannot be used to represent weighted
    edges only the unweighted edges can be represented.
    """
    def __init__(self, num_vertices, directed=False):
        super(AdjacencySetGraph, self).__init__(num_vertices, directed)

        self.vertices = [Node(vertex_id) for vertex_id in range(num_vertices)]

    def add_edge(self, v1, v2, weight=1):

        # check if the vertices are valid
        if v1 >= self.num_vertices or v2 >= self.num_vertices or v1 < 0 or v2 < 0:
            raise ValueError("Vertices %d and %d are out of bounds" % (v1, v2))

        if weight != 1:
            raise ValueError("An adjacency set cannot represent edge weight > 1")

        self.vertices[v1].add_edge(v2)

        if not self.directed:
            self.vertices[v2].add_edge(v1)

    def get_adjacent_vertices(self, v):

        # check if the vertex is valid
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex %d is out of bounds" % v)

        return self.vertices[v].get_adjacency_set()

    def get_in_degree(self, v):

        # check if the vertex is valid
        if v >= self.num_vertices or v < 0:
            raise ValueError("Vertex %d is out of bounds" % v)

        in_degree = 0

        for node in range(self.num_vertices):
            if v in self.get_adjacent_vertices(node):
                in_degree += 1

        return in_degree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        for from_vertex in range(self.num_vertices):
            for to_vertex in self.get_adjacent_vertices(from_vertex):
                print(from_vertex, "-->", to_vertex)


g = AdjacencySetGraph(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(2, 3)


for i in range(4):
    print("Adjacent to:", i, g.get_adjacent_vertices(i))

# display the in_degree for each vertex in the graph
for i in range(4):
    print("In degree: ", i, g.get_in_degree(i))

# display the weight for each edge in the graph
for i in range(4):
    for j in g.get_adjacent_vertices(i):
        print("Edge weight: ", i, " ", j, "weight: ", g.get_edge_weight(i, j))

# display the graph
g.display()
