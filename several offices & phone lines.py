def minDistByFW(cost, v):
    INF = float('inf')

    dist = [[INF] * v for _ in range(v)]
    for i in range(v):
        for j in range(v):
            if i == j:
                dist[i][j] = 0  
            elif cost[i][j] > 0:
                dist[i][j] = cost[i][j]

    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
def main():
    v = int(input("Enter number of offices (vertices): "))
    e = int(input("Enter number of phone lines (edges): "))

    cost = [[0] * v for _ in range(v)]

    for i in range(e):
        while True:
            a, b, w = map(int, input(f"Enter initial office, final office, and cost for line {i + 1}: ").split())
            if 1 <= a <= v and 1 <= b <= v:
                break
            else:
                print(f"Invalid node input. Please enter offices between 1 and {v}.")

        cost[a-1][b-1] = w
        cost[b-1][a-1] = w

    print("\nAdjacency matrix representation of the phone lines (graph):")
    for row in cost:
        print(' '.join(map(str, row)))

    dist = minDistByFW(cost, v)

    print("\nThe shortest connection costs between every pair of offices:")
    for i in range(v):
        for j in range(v):
            if dist[i][j] == float('inf'):
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
