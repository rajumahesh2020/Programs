# Graph here is undirected

# breadth first search, explore all neighbours of current node(breadth), before moving to next node


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}

    def add_edge(self, node1, node2):
        if node1 in self.adj_list:
            self.adj_list[node1].append(node2)
        else:
            self.adj_list[node1] = [node2]
        if node2 in self.adj_list:
            self.adj_list[node2].append(node1)
        else:
            self.adj_list[node2] = [node1]

    def bfs(self, start):
        visited = [0]*self.vertices
        visited[1] = 1
        queue = []
        bfs_list = []
        queue.append(start)
        while len(queue):
            current = queue.pop(0)
            bfs_list.append(current)
            for node in self.adj_list[current]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = 1
        return bfs_list


if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 4)
    graph.add_edge(3, 5)
    print(graph.bfs(1))
