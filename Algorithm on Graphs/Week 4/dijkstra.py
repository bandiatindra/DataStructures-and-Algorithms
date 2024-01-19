#Uses python3

import sys
import queue
import heapq

def distance(adj, cost, s, t):
    #write your code here
    n = len(adj)
    dist = [float('inf')]*n
    #prev = []*n
    dist[s] = 0
    
    priority_queue = []
    heapq.heappush(priority_queue, (0,s))

    while len(priority_queue)!=0:
        w, u = heapq.heappop(priority_queue)

        for i in range(len(adj[u])):
            if dist[adj[u][i]] > dist[u] + cost[u][i]:
                dist[adj[u][i]] = dist[u] + cost[u][i]
                # prev[v] = u
                heapq.heappush(priority_queue, (dist[adj[u][i]],adj[u][i]))



    if dist[t] ==  float('inf'):
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
