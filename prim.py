class Priority_Queue:
    def __init__(self):
        self.queue = []

    def add_in_queue(self, item):
        self.queue.append(item)

    def pop_element(self):
        for i in range(len(self.queue) // 2, -1, -1):
            self.build_heap(i)
        item = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop(-1)
        return item

    def build_heap(self, start):
        size = len(self.queue)
        while True:
            left_child = 2 * start + 1
            right_child = 2 * start + 2
            min = start
            if left_child < size and self.queue[left_child][0] < self.queue[min][0]:
                min = left_child
            if right_child < size and self.queue[right_child][0] < self.queue[min][0]:
                min = right_child
            if min != start:
                self.queue[start], self.queue[min] = self.queue[min], self.queue[start]
                start = min
            else:
                break


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}

    def add_edge(self, node1, node2, weight):
        if node1 in self.adj_list:
            self.adj_list[node1].append([node2, weight])
        else:
            self.adj_list[node1] = [[node2, weight]]
        if node2 in self.adj_list:
            self.adj_list[node2].append([node1, weight])
        else:
            self.adj_list[node2] = [[node1, weight]]

    def Prim_Algo(self):
        queue = Priority_Queue()
        keys = [float("inf")] * (self.vertices + 1)
        # Har vertices ko apne khud ka papa bhi bana sakta hai, but yaha par uski jarurat nahi hai
        parent = [-1] * (self.vertices + 1)
        #mst is the final mst
        mst = []
        # Apna pahla vertex 1 hai, na ki 0
        keys[1] = 0
        queue.add_in_queue([keys, 1])
        while len(mst) < self.vertices:
            temp = queue.pop_element()
            while temp[1] in mst:
                temp = queue.pop_element()
            mst.append(temp[1])
            for neighbour in self.adj_list[temp[1]]:
                if neighbour not in mst and keys[neighbour[0]] > neighbour[1]:
                    keys[neighbour[0]] = neighbour[1]
                    queue.add_in_queue([keys, neighbour[0]])
                    parent[neighbour[0]] = temp[1]
        for i in mst:
            if parent[i] != -1:
                print((parent[i], i))


if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 4, 2)
    graph.add_edge(2, 3, 3)
    graph.add_edge(3, 4, 3)
    graph.add_edge(3, 5, 4)
    # print(graph.adj_list)
    graph.Prim_Algo()
