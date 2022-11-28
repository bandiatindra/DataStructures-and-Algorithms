#Uses python3

import sys


def number_of_components(adj):
    result = 0
    
    n = len(adj)
    visited = [False]*n

    def Explore (adj, visited, vertex):
        visited[vertex] = True
        for w in adj[vertex]:
            if visited[w] == False:
                Explore(adj, visited, w)
        return visited
    
    for  vertex in range(n):
        if visited[vertex] == False:
            result = result + 1
            visited = Explore (adj, visited, vertex)
        else:
            continue
    
    


    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
