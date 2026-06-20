def isSafe(node, color, graph, n, col):
    for k in range(n):
        # If there is an edge and adjacent node has same color
        if graph[node][k] == 1 and color[k] == col:
            return False
    return True

# Backtracking function
def solve(node, color, m, n, graph):

    # All nodes are colored successfully
    if node == n:
        return True

    # Try every color from 1 to m
    for col in range(1, m + 1):

        # Check whether current color is valid
        if isSafe(node, color, graph, n, col):

            # assign color
            color[node] = col

            # recurse for next node
            if solve(node + 1, color, m, n, graph):
                return True

            # backtrack
            color[node] = 0

    return False


# Main function
def graphColoring(graph, m, n):

    # 0 means uncolored
    color = [0] * n

    return solve(0, color, m, n, graph)
n = 4
m = 3

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

if graphColoring(graph, m, n):
    print("Graph can be colored with", m, "colors")
else:
    print("Graph cannot be colored with", m, "colors")