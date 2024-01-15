#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    used[x] = 1
    for w in adj[x]:
        if used[w] == 0:
            dfs(adj, used, order, w)
    order.append(x)
    pass


def toposort(adj):
    used = [0] * len(adj)
    order = []
    n = len(adj)
    for v in range (n):
        if used[v] == 0:
            dfs(adj, used, order, v)
    #write your code here
    return order[::-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

