class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        #Check columns are correct
        for i in range(len(board)):
            col_dict = {}
            for j in range(len(board)):
                if board[i][j]!='.':
                    if board[i][j] in col_dict:
                        return False
                    else:
                        col_dict[board[i][j]] = 1
        #Check rows are correct
        for i in range(len(board)):
            col_dict = {}
            for j in range(len(board)):
                if board[j][i]!='.':
                    if board[j][i] in col_dict:
                        return False
                    else:
                        col_dict[board[j][i]] = 1
        
        #Check if every 3*3 grid have any duplicates. We create a dictionary with keys as (i//3,j//3),
        # So basically it will have (0,0), (0,1), (0,2), (1,0) ...(3,3) as keys. 
        # Each key will have a list of values - which will be elements inside the grid.
        # Then we search this entire key's elements for all 3*3 grid ellemtns in our array 
        # If we find it return False. Otherwise contniue
        grid = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!='.':
                    if (i//3,j//3) not in grid.keys():

                        grid[(i//3,j//3)] = []
                    
                    if board[i][j] in grid[(i//3 , j//3)]:
                        return False
                    
                    grid[(i//3,j//3)].append(board[i][j])
                    
                        
        return True

        
        
                    
