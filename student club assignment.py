import heapq
N = 4 
class Node:
    def __init__(self, student, club, assigned, parent):
        self.parent = parent
        self.studentID = student
        self.clubID = club
        self.assigned = assigned[:]
        if club != -1:
         self.assigned[club] = True
        self.pathCost = 0
        self.cost = 0

class CustomHeap:
    def __init__(self):
        self.heap = []

    def push(self, node):
        heapq.heappush(self.heap, (node.cost, node))

    def pop(self):
        return heapq.heappop(self.heap)[1] if self.heap else None

def calculate_cost(cost_matrix, student, assigned):
    cost = 0
    available = [True] * N
    for i in range(student + 1, N):
        min_val, min_index = float('inf'), -1
        for j in range(N):
            if not assigned[j] and available[j] and cost_matrix[i][j] < min_val:
                min_index = j
                min_val = cost_matrix[i][j]
        if min_index != -1:
            cost += min_val
            available[min_index] = False
    return cost

def print_assignments(node):
    if node.parent is None:
        return
    print_assignments(node.parent)
    print(f"Assign Student {chr(node.studentID + ord('A'))} to Club {node.clubID + 1}")

def find_min_cost(cost_matrix):
    pq = CustomHeap()
    root = Node(-1, -1, [False] * N, None)
    pq.push(root)

    while pq:
        min_node = pq.pop()
        student = min_node.studentID + 1
        if student == N:
            print_assignments(min_node)
            return min_node.cost

        for club in range(N):
            if not min_node.assigned[club]:
                child = Node(student, club, min_node.assigned, min_node)
                child.pathCost = min_node.pathCost + cost_matrix[student][club]
                child.cost = child.pathCost + calculate_cost(cost_matrix, student, child.assigned)
                pq.push(child)

def get_cost_matrix():
    global N
    N = int(input("Enter the number of students/clubs: "))
    return [list(map(int, input(f"Row {i + 1}: ").split())) for i in range(N)]

if __name__ == "__main__":
    cost_matrix = get_cost_matrix()
    optimal_cost = find_min_cost(cost_matrix)
    if optimal_cost is not None:
        print(f"\nOptimal Cost is {optimal_cost}")
    else:
        print("\nNo optimal solution found.")
