class UnionFind():
    def __init__(self, n):
        
        self.rank = [1] * n
        self.parent = list(range(n))
        self.count = n
    
    def Find(self, i):
        if i != self.parent[i]:
                self.parent[i] = self.Find(self.parent[i])
        return self.parent[i]
    
    def Union(self, i, j):
        i_parent = self.Find(i)
        j_parent = self.Find(j)
        # Firs time we find 2 elements in the same set it means that they already are connected and current edge is redundant edge!
        if i_parent == j_parent:
            return False
        if self.rank[i_parent] < self.rank[j_parent]:
            self.parent[i_parent] = j_parent
            self.count -=1
        else:
            self.parent[j_parent] = i_parent
            self.count -=1
            if self.rank[i_parent] == self.rank[j_parent]:
                self.rank[i_parent] = self.rank[i_parent] + 1
                
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        uf = UnionFind(1001)
        for edge in edges:
            if uf.Union(edge[0],edge[1]) == False:
                return edge
            
        