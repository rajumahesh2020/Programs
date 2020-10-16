# Depth first search traversel, depth mai ghus jao aur fir backtracking ki vajah se saare nodes ko explore kar lo -> recursive
#      1
#    /   \
#   /     \
#  /       \
# 2----3----4
#      |
#      5


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

    def dfs(self, start, visited):
        visited[start] = 1
        print(start, end=" ")
        for node in self.adj_list[start]:
            if not visited[node]:
                self.dfs(node, visited)

    # Agar disconnected graph hoga, then there there will be various connected components and this graph will make, sure that every connected component is traversed. No. of functions calls se tu, ye bhi pata laga sakta hai ki number of connected components kitne hai
    def dfs_traverser(self):
        visited = [0]*self.vertices
        for vertex in self.adj_list:
            if not visited[vertex]:
                self.dfs(vertex, visited)


if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 4)
    graph.add_edge(3, 5)
    graph.dfs_traverser()
