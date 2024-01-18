#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    n = len(adj)
    dist = [float('inf')]*n
    dist[s] = 0
    queue = []
    queue.append(s)
    while len(queue)!=0:
        u = queue[0]
        queue.pop(0)
        for i in range(len(adj[u])):
            if dist[adj[u][i]] == float('inf'):
                queue.append(adj[u][i])
                dist[adj[u][i]] = dist[u] + 1

    if dist[t] ==  float('inf'):
        return -1
    else:
        return dist[t]



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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
