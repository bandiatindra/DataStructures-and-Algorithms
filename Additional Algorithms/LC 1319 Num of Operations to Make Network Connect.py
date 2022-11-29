class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        m = len (connections)
        if m < n-1:
            return -1
        adj = [[] for _ in range(n)]
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        visited = [False]*n
        result = 0
        for  vertex in range(n):
            if visited[vertex] == False:
                result = result + 1
                visited = self.Explore (adj, visited, vertex)
            else:
                continue
        return result - 1
        
    def Explore (self, adj, visited, vertex):
        visited[vertex] = True
        for w in adj[vertex]:
            if visited[w] == False:
                self.Explore(adj, visited, w)
        return visited
        