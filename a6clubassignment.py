import heapq

class Node:
    def __init__(self, student, club, assigned, cost, parent=None):
        self.student = student
        self.club = club
        self.assigned = assigned[:]
        if club != -1:
         self.assigned[club] = True
        self.cost = cost
        self.parent = parent

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, node):
        heapq.heappush(self.queue, (node.cost, node))

    def pop(self):
        return heapq.heappop(self.queue)[1] if self.queue else None

def calculate_cost(matrix, student, assigned):
    cost = 0
    for i in range(student + 1, len(matrix)):
        cost += min(matrix[i][j] for j in range(len(matrix)) if not assigned[j])
    return cost

def print_assignments(node):
    if node.parent:
        print_assignments(node.parent)
        print(f"Student {chr(node.student + ord('A'))} → Club {node.club + 1}")

def find_min_cost(matrix):
    n = len(matrix)
    root = Node(-1, -1, [False] * n, 0)
    pq = PriorityQueue()
    pq.push(root)

    while pq.queue:
        node = pq.pop()
        student = node.student + 1
        if student == n:
            print_assignments(node)
            return node.cost

        for club in range(n):
            if not node.assigned[club]:
                path_cost = node.cost + matrix[student][club]
                estimated_cost = path_cost + calculate_cost(matrix, student, node.assigned)
                pq.push(Node(student, club, node.assigned, estimated_cost, node))

def get_cost_matrix():
    n = int(input("Enter number of students/clubs: "))
    print("Enter cost matrix:")
    return [list(map(int, input().split())) for _ in range(n)]

if __name__ == "__main__":
    cost_matrix = get_cost_matrix()
    optimal_cost = find_min_cost(cost_matrix)
    print(f"\nOptimal Cost: {optimal_cost}")
