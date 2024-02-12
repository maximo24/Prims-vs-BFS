import random
import BFS
import MST

# Calculating the average difference of BFS and Prims total weight
def calculate_average_diff(diffList, k):
    total = 0
    for i in range(len(diffList)):
        total += diffList[i]
    total = total / k
    return total


# Print the average difference of BFS and Prims total weight
def report_average_diff(reportDiffList):
    print("\n\n Report the average value of Diff for each value of n. \n")
    n = 20
    print("\n Value of n\t|   Average Val of Diff")
    for i in range(len(reportDiffList)):
        print("    ", n, "\t|\t", reportDiffList[i])
        n += 20


diffList = []
reportDiffList = []

for n in range(20, 61, 20):
    print("\n For n = ", n)
    k = int(input("\n Enter value of k repetition : "))
    temp = k

    # a list to track selected vertices and will become true otherwise false
    selectedVertices = [0 for i in range(n)]

    # set total number of edges to 0
    totalEdge = 0
    selectedVertices[0] = True
    while (temp > 0):
        # Filling the graph with the random value ranging from 0 to 30
        graph = [[random.randint(0, 30) for i in range(n)] for j in range(n)]

        # Applying BFS algorithm on the graph
        b = BFS.bfs(graph, 0, n)

        # print("\nBFS weight : ", B)

        # Applying Prim's algorithm on the graph
        p = MST.prim_algorithm(graph, n, selectedVertices, totalEdge)

        # print("\nPrim weight :", P, "\n")

        diff = ((b - p) / p) * 100
        # print(Diff,"%")
        diffList.append(diff)
        temp -= 1

    diffAvg = calculate_average_diff(diffList, k)

    # print("Diff average : ", Diff_Avg)

    reportDiffList.append(diffAvg)
    diffList.clear()

report_average_diff(reportDiffList)
