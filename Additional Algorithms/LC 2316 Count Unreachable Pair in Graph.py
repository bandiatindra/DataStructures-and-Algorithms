class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
    
        
        size = []
        visited = [0]*n
        
        for  vertex in range(n):
            if visited[vertex] == 0:
                count = [0]
                
                self.Explore (adj, visited, vertex, count)
                size.append(count[0])
                
            else:
                continue
        res = 0
        for val in size:
            remaining = n - val
            res = res + val*remaining
        return int(res/2)

    def Explore (self, adj, visited, vertex, count):
        visited[vertex] = 1
        count[0] = count[0] + 1
        
        for w in adj[vertex]:
            if visited[w] == 0:
                self.Explore(adj, visited, w, count)
        return count[0]
        
        
    
    
    
    
        