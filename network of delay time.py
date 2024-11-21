def min_distance(distances, visited):
    min_val = float('inf')
    min_index = -1
    for i in range(len(distances)):
        if distances[i] < min_val and i not in visited:
            min_val = distances[i]
            min_index = i
    return min_index

def networkDelayTime(graph, N, K):
   
    distances = [float('inf')] * N
    visited = set()
    distances[K - 1] = 0
    
    for _ in range(N):
        current_node = min_distance(distances, visited)
        if current_node == -1:  
            break
        visited.add(current_node)
        
        for neighbor in range(N):
            if graph[current_node][neighbor] > 0 and neighbor not in visited:
                new_distance = distances[current_node] + graph[current_node][neighbor]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    
    max_distance = max(distances)
    return max_distance if max_distance < float('inf') else -1

def main():
    N = int(input("Enter the number of nodes (N): "))
    M = int(input("Enter the number of edges (M): "))
    K = int(input("Enter the starting node (K): "))
    
    graph = [[0] * N for _ in range(N)]
    
    print("Enter the edges (u, v, w) where u and v are nodes, and w is the weight:")
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u - 1][v - 1] = w  
    
    result = networkDelayTime(graph, N, K)
    
    print("The minimum time to send the signal to all nodes is:", result)

if __name__ == "__main__":
    main()
