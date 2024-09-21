graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 8), ('E', 9)],
    'E': [('B', 5), ('C', 7), ('D', 9)]
}

def get_min_node(taken_nodes, taken_edges):
    result = None
    min_weight = float('inf')
    
    for node in taken_nodes:
        for neighbor, weight in graph[node]:
            if not ((node, neighbor) in taken_edges or (neighbor, node) in taken_edges) and weight < min_weight and neighbor not in taken_nodes:
                min_weight = weight
                result = node, neighbor
    return result

# Can be improved using priority queue.
def prims_mst(graph, start_node):
    taken_nodes = set([start_node])
    taken_edges = set()
    mst = {}
    total_nodes = len(graph)

    while len(taken_nodes) < total_nodes:
        result = get_min_node(taken_nodes, taken_edges)
        if result:
            node , next_node = result
            taken_edges.add(next_node)
            taken_nodes.add(next_node)
            
            if node in mst and isinstance(mst[node], list):
                mst[node].append(next_node)
            else:
                mst[node] = [next_node]
    return mst

if __name__ == "__main__":
    mst = prims_mst(graph=graph, start_node="A")
    
    for key, value in mst.items():
        print(f"{key}-> {','.join(value)}")
    # A-> B,D
    # B-> C,E