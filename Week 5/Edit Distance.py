# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s) 
    n = len (t) 
    #Always intitalize 2d Array like this! 
    D = [[0] * (n+1) for i in range(m+1)] 
    
    #Initialize edges
    for i in range(m+1):
       D[i][0] = i
       for j in range(n+1):
           D[0][j] = j
           
  
    for i in range (1, m+1):
        for j in range (1,n+1):
            insert = D[i][j-1] + 1
            delete = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1

            if s[i-1] == t[j-1]:
                D[i][j] = min(insert,delete,match)
            else:
                D[i][j] = min(insert,delete,mismatch)

    return D[m][n]
    

    

if __name__ == "__main__":
    print(edit_distance(input(), input()))