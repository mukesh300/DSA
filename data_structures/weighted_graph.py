class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end, weight in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append((end, weight))
            else:
                self.graph_dict[start] = [(end, weight)]

    def shortest_path(self, start, end, path=[]):
        path = path+["start"]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_paths(node, end, path)
                for p in new_path:
                    paths.append(p)


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Pune", 300),
        ("Mumbai", "Surat", 200),
        ("Surat", "Bangaluru", 500),
        ("Pune", "Hyderabad", 100),
        ("Pune", "Mysuru", 600),
        ("Hyderabad", "Bangaluru", 100),
        ("Hyderabad", "Chennai", 400),
        ("Mysuru", "Bangaluru", 700),
        ("Chennai", "Bangaluru", 300)
    ]
    route_graph = Graph(routes)
    print(route_graph.graph_dict)

    start, end = "Mumbai", "Bangaluru"


