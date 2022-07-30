# python3

import sys
import threading


def compute_height(n, parents):
    # Replace this code with a faster implementation
   
    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height

    # Code to create a tree using the input data
    class Node:
        def __init__(self, data):
            self.children = []
            self.data = data
            
        def addChild(self, child):
            self.children.append(child)
    
    list_of_nodes = []
    for i in range(n):
        list_of_nodes.append(Node(i))

    for i in range(n):

        if parents[i] == -1:
            root = list_of_nodes[i]
        else:
            list_of_nodes[parents[i]].addChild(list_of_nodes[i])
    
    def calculateHeight (root):
        from collections import deque
        
        if root is None:
            return 0
        if len(root.children) == 0:
            return 1
        else:
            
            q = deque()
            q.append(root)
            depthQ = deque()
            depthQ.append(1)
            while q:
                
                node = q.popleft()
                depth = depthQ.popleft()
                
                if len(node.children)!=0:
                    
                    for i in range(len(node.children)):
                        q.append(node.children[i])
                        depthQ.append(depth+1)
                        
                        
        return depth

    tree_height = calculateHeight(root)

    return tree_height



def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()