#
# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where 
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
#

def bipartite(G):
    # your code here
    # return a set
    total_nodes = []
    set1 = []
    set2 = []
    for node in G:
        total_nodes.append(node)
        set1.append(node)
        break
    while len(total_nodes) > 0:
        node = total_nodes.pop()
        for neighbor in G[node]:
            if node in set1 and neighbor not in set2:
                set2.append(neighbor)
                total_nodes.append(neighbor)
            if node in set2 and neighbor not in set1:
                set1.append(neighbor)
                total_nodes.append(neighbor)
    for elem in set1:
        if elem in set2:
            return None
    return set2


########
#
# Test

def make_link(G, node1, node2, weight=1):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = weight
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = weight
    return G


def test():
    edges = [(1, 2), (2, 3), (1, 4), (2, 5),
             (3, 8), (5, 6)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert (g1 == set([1, 3, 5]) or
            g1 == set([2, 4, 6, 8]))
    edges = [(1, 2), (1, 3), (2, 3)]
    G = {}
    for n1, n2 in edges:
        make_link(G, n1, n2)
    g1 = bipartite(G)
    assert g1 == None
