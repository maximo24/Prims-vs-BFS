# set infinity to maximum value

INF = 9999999


def prim_algorithm(graph, vertices, selectedVertices, totalEdge):
    count = 0
    print("\n Edge  : Weight\n")

    # the toal no. of egdes in MST will always less than Vertices - 1
    while (vertices - 1 > totalEdge):
        minValue = INF
        temp1 = temp2 = 0
        for i in range(vertices):
            # Check if selected vertex value is true
            if selectedVertices[i]:
                for j in range(vertices):
                    # Check if not in selected vertex is true and there exists an edge
                    if (graph[i][j] and (not selectedVertices[j])):
                        if minValue > graph[i][j]:
                            # set min value to the weight of the vertex
                            minValue = graph[i][j]
                            temp1 = i
                            temp2 = j

        # calculating the total weight of the graph
        count += graph[temp1][temp2]
        # print the edge with the weight
        print(temp1, "--", temp2, ": ", graph[temp1][temp2])
        selectedVertices[temp2] = True
        totalEdge += 1
    return count


# number of vertices in graph
vertices = 6

graph = [[0, 15, 0, 7, 10, 0],
         [15, 0, 9, 11, 0, 9],
         [0, 9, 0, 0, 12, 7],
         [7, 11, 0, 0, 8, 14],
         [10, 0, 12, 8, 0, 8],
         [0, 9, 7, 4, 8, 0]]

# a list to track selected vertices and will become true otherwise false
selectedVertices = [0, 0, 0, 0, 0, 0]
selectedVertices[0] = True

# set total number of edges to 0
totalEdge = 0

totalWeight = prim_algorithm(graph, vertices, selectedVertices, totalEdge)
print("\nTotal weight of the edges : ", totalWeight, "\n")
