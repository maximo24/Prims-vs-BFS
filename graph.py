import random


class graph:
    def __init__(self):
        self.vertexGraph = {}
        self.edgesWeight = {}

    # Return the vertices
    def vertices(self):
        return list(self.vertexGraph.keys())

    # Return the edges
    def edges(self):
        return self.edgesWeight.keys()

    # Return the weight of the edge
    def edge_weight(self):
        return self.edgesWeight

    # Add new vertex
    def insert_vertex(self, vertex):
        if vertex not in self.vertexGraph:
            self.vertexGraph[vertex] = []

    # Add the edge to the vertices
    def insert_edge(self, edge, weight):
        edge = set(edge)
        if len(edge) <= 1:
            return False
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.vertexGraph:
            self.vertexGraph[vertex1].append(vertex2)
        else:
            self.vertexGraph[vertex1] = [vertex2]
        self.edgesWeight[tuple(edge)] = weight

    # Print the vertices and edges of the graph
    def __str__(self):
        graphResult = "\n\n The vertices of the graph :-\n\n"
        for k in self.vertexGraph:
            graphResult += str(k) + " "
        graphResult += "\n\n The edges of the graph with weights :-\n\n"
        for edge in self.edgesWeight:
            graphResult += str(edge) + ": " + str(self.edgesWeight[edge]) + "\n"
        return graphResult


# testing

g = graph()
n = int(input("\nEnter value of n : "))
vertices = list(range(1, n + 1))
for i in vertices:
    g.insert_vertex(i)
for i in range(2, n + 1):

    # Randomly selects a number between 1 1o i-1
    x = random.randint(1, i - 1)

    # Randomly chooses x vertex from vertices
    S = random.sample(vertices, x)
    for s in S:
        # Randomly generating weight between 10 to 100
        w = random.randint(10, 100)
        g.insert_edge((i, s), w)

# print graph
print("\n\nThe resulting Graph :-", g)
