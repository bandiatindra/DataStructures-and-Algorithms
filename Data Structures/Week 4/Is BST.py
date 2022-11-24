#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Instead of checking each node, we will do inorder traversal. Inorder traversal gives the array in ascending order if the BST is correctly constructed
  # So we will compare our output with sorted(array) of the inorder result of the BST. If they match then BST is constructed correctly.

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
        while index!= -1:
            stack.append(key[index])
            index_stack.append(index)
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
