#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    n = len(adj)
    visited = [False]*n

    def Explore (v, adj, visited):
        visited[v] = True
        for w in adj[v]:
            if visited[w] == False:
                Explore(w, adj, visited)
        return visited

    visited = Explore(x, adj, visited)
    if visited[y] == True:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:] 
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
