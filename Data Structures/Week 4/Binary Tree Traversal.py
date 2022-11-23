# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    stack = []
    index = 0
    index_stack =[]
    while True:
        while index!= -1:
            stack.append(self.key[index])
            index_stack.append(index)
            index = self.left[index]
            
        if not stack:
            return self.result

        self.result.append(stack.pop())
        index = index_stack.pop()
        index = self.right[index]
        
    

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    # Iterative Approach
    self.result.append(self.key[0])
    stack = []
    stack.append(self.right[0])
    stack.append(self.left[0])
    while stack!= []:
        index = stack.pop()
        if index >=0:
            self.result.append(self.key[index])
            if self.right[index]!= -1:
                stack.append(self.right[index])
            if self.left[index]!= -1:
                stack.append(self.left[index])
                
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    # Iterative Aproach like Pre-order, with variation to get right first then left AND print the tree in reverse order. 
    self.result.append(self.key[0])
    stack = []
    stack.append(self.left[0])
    stack.append(self.right[0])

    while stack!= []:
        index = stack.pop()
        if index >=0:
            self.result.append(self.key[index])
            if self.left[index]!= -1:
                stack.append(self.left[index])        
            if self.right[index]!= -1:
                stack.append(self.right[index])
        
                
    return self.result[::-1]

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
