import collections
import random


# BFS algorithm
def bfs(graph, root, n):
    total = 0
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    totalV = n
    while queue:
        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(vertex, end="  ")
        for i in range(totalV):
            for neighbour in range(totalV):
                # If not visited, mark it as visited
                if neighbour not in visited and graph[i][neighbour]:
                    visited.add(neighbour)
                    # enqueue the neighbour
                    queue.append(neighbour)
                    # calculating the total weight
                    total += graph[i][neighbour]
    return total


# testing

graph = [[0, 15, 0, 7, 10, 0],
         [15, 0, 9, 11, 0, 9],
         [0, 9, 0, 0, 12, 7],
         [7, 11, 0, 0, 8, 14],
         [10, 0, 12, 8, 0, 8],
         [0, 9, 7, 4, 8, 0]]

vertices = [0, 1, 2, 3, 4, 5]

x = random.randint(0, 5)
print("\n The random starting vertex : ", x)
print("\n The path created after Breadth First Traversal :-\n ")
totalWeight = bfs(graph, x, len(vertices))
print("\n\n\n Total weight : ", totalWeight, "\n\n")
