from queue import PriorityQueue

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]

    def best_first_search(self, start, goal):
        explored = []
        pq = PriorityQueue()
        pq.put((0, start))
        parents = {start: None}

        while not pq.empty():
            current = pq.get()[1]

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parents[current]
                path.reverse()
                print(f"Best-First Search path: {path}")
                return path

            explored.append(current)

            for neighbor, weight in self.get_neighbors(current):
                if neighbor not in explored and neighbor not in [i[1] for i in pq.queue]:
                    parents[neighbor] = current
                    pq.put((self.h(neighbor), neighbor))

        print("Path not found!")
        return None

adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}

graph1 = Graph(adjacency_list)
graph1.best_first_search('A', 'D')
