graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 8), ('E', 9)],
    'E': [('B', 5), ('C', 7), ('D', 9)]
}

def get_min_node(taken_nodes, taken_edges):
    result = None
    _min = ("X", 1000000)
    node = None
    for node in taken_nodes:
        for edge in graph[node]:
            if (node, edge[0]) in taken_edges or (edge[0], node) in taken_edges: 
                continue
            if edge[1] < _min[1] and edge[0] not in taken_nodes:
                _min = edge
                result = node, _min
    return result


def prims_mst(graph, start_node):
    taken_nodes = set([start_node])
    taken_edges = set()
    mst = {}
    total_nodes = len(graph)

    while len(taken_nodes) < total_nodes:
        result = get_min_node(taken_nodes, taken_edges)
        if result:
            node , min_edge = result
            taken_edges.add(min_edge)
            taken_nodes.add(min_edge[0])
            
            if node in mst and isinstance(mst[node], list):
                mst[node].append(min_edge)
            else:
                mst[node] = [min_edge]
    return mst

if __name__ == "__main__":
    mst = prims_mst(graph=graph, start_node="A")
    print(mst)