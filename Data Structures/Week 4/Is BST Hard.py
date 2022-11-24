#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
# Edge case when there is only one node.
    if len(tree) <= 1:
        return True
    
    n = len(tree)
    key = [0 for i in range(n)]
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    for i in range(n):
        key[i] = tree[i][0]
        left [i] = tree[i][1]
        right [i] = tree[i][2]

    result = []
    
    stack = []
    index = 0
    index_stack =[]
    
    while True:
        count_key = {} 
        #Let's track the occurence of a node in the left branch. If it exits and we are seeing it again, then its not BST. 
        #We should however re-start this dictionary everytime a right node is observed because its okay to have the same node in the right tree.
        while index!= -1:
            stack.append(key[index])
            index_stack.append(index)
            if key[index] in count_key:
                return False
            else:
                count_key[key[index]] = 1
            index = left[index]
            
        if not stack:
            if result == sorted(result):
                return True
            else:
                return False

        result.append(stack.pop())
        index = index_stack.pop()
        index = right[index]



def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
