class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue((starting_vertex, [starting_vertex]))
        while q.size() > 0:
            v = q.dequeue()
            for neighbour in self.vertices[v[0]]:
                if neighbour == destination_vertex:
                    return v[1] + [neighbour]
                else:
                    q.enqueue((neighbour, v[1] + [neighbour]))


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    path_store = []
    unique_set = set()
    # make a set to get all unique values
    for tup in ancestors:
        unique_set.add(tup[0])
        unique_set.add(tup[1])
    # make a node for eah new value
    for value in unique_set:
        graph.add_vertex(value)
    # Build edges in reverse
    for tup in ancestors:
        graph.add_edge(tup[1], tup[0])
    print(graph.vertices)
    # Do a BFS (storing the path)
    earliest_ancestor = -1
    for node in graph.vertices:
        if graph.bfs(starting_node, node) is not None:
            path = graph.bfs(starting_node, node)
            print(node)
            print(path)
            if len(path) > len(path_store):
                path_store = path.copy()
            elif len(path) == len(path_store):
                if path[-1] < path_store[-1]:
                    path_store = path.copy()

            earliest_ancestor = path_store[-1]
            # If the path is longer or equal and the value is smaller, or if the path is longer)
    return earliest_ancestor


ancestors_example = [(1, 3), (2, 3), (3, 6), (5, 6),
                     (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(ancestors_example, 6))
