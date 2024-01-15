#Uses python3

import sys


def acyclic(adj):
       
    n = len(adj)
    visited = [False]*n
    current_stack = [False]*n           
    
            
    for  vertex in range(n):
        if visited[vertex] == False:
            if Explore (adj, visited, current_stack, vertex) ==1:
                return 1

    return 0

def Explore (adj, visited, current_stack, vertex):
       
       visited[vertex] = True
       current_stack[vertex] = True
       
        
       for w in adj[vertex]:
           
           if visited[w] == False:
               if Explore(adj, visited, current_stack, w) == 1:
                   return 1
               
           elif current_stack[w] == True:
                return 1
               
       current_stack[vertex] = False
       return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
