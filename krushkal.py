class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edge_list = []
    # weight ke sath deal karna ho to adj_list se better, array hi hai, kyuki sorting vagerah asani se ho jayegi

    def add_edge(self, node1, node2, weight):
        self.edge_list.append([node1, node2, weight])

    def parent_finder(self, parent, node):
        # Node khud apna baap ho to, sidha use hi bhej diya
        if parent[node] == node:
            return node

        # Node ka papa koi aur hai, kya us koi aur ka bhi koi papa hai, hai to nikalo, kyuki apan ko sabse bada wala papa chahiye, isliye recursive call
        return self.parent_finder(parent, parent[node])

    def union(self, rank, parent, node1, node2):
        node1_parent = self.parent_finder(parent, node1)
        node2_parent = self.parent_finder(parent, node2)

        if rank[node1_parent] < rank[node2_parent]:
            parent[node1_parent] = node2_parent
        elif rank[node1_parent] > rank[node2_parent]:
            parent[node2_parent] = node1_parent
        else:
            parent[node2_parent] = node1_parent
            rank[node1_parent] += 1

    def Krushkal(self):
        new_edge_list = self.edge_list.copy()
        new_edge_list.sort(key=lambda x: x[2])

        # MST ka final result yaha aayega
        MST = []

        # For keeping track ki kiska papa kaun hai
        parent = [0]*(self.vertices+1)

        # relation jodne ke samay (edge connect karne se pahle) kaun kiska papa banega, wo unki rank se decide hoga
        rank = [0]*(self.vertices+1)

        # Sab individual vertices ko apne aap ka hi papa bana ke liye, kyuki MST banane se pahle sab anaat hai!
        for i in range(self.vertices):
            parent[i] = i

        # Chalo ab relation banate hai(MST)
        count = 0
        while count < self.vertices:
            count += 1
            temp = new_edge_list.pop(0)
            node1, node2, weight = temp
            node1_parent = self.parent_finder(parent, node1)
            node2_parent = self.parent_finder(parent, node2)

            # ab dono ke parent different hone chahiye, otherwise wo cycle bana lenge
            if node1_parent != node2_parent:
                MST.append(temp)

                # ab naya relation banega dono vertices mai, rank par aadharit
                self.union(rank, parent, node1, node2)

        return MST


if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 4, 2)
    graph.add_edge(2, 3, 3)
    graph.add_edge(3, 4, 3)
    graph.add_edge(3, 5, 4)
    print(graph.Krushkal())
