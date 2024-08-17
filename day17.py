"""
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Solved
Hard
Topics
Companies
Hint
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
    """
    
    
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        alice_uf, bob_uf = UnionFind(n + 1), UnionFind(n + 1)
        removed_edges = alice_edges = bob_edges = 0

        for t, u, v in sorted(edges, reverse=True):
            if t == 3:
                if alice_uf.union(u, v): 
                    bob_uf.union(u, v)
                    alice_edges += 1
                    bob_edges += 1
                else:
                    removed_edges += 1
            elif t == 1:
                if not alice_uf.union(u, v):
                    removed_edges += 1
                else:
                    alice_edges += 1
            elif t == 2:
                if not bob_uf.union(u, v):
                    removed_edges += 1
                else:
                    bob_edges += 1

        if alice_edges == bob_edges == n - 1:
            return removed_edges
        return -1
