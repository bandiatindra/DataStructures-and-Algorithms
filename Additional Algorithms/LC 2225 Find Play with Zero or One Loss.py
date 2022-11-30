class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_count = {}
        lost_count = {}
        for i in range(len(matches)):
            if matches[i][0] in win_count:
                win_count[matches[i][0]] +=1
            else: 
                win_count[matches[i][0]] = 1
            if matches[i][1] in lost_count:
                lost_count[matches[i][1]] +=1
            else:
                lost_count[matches[i][1]] = 1
        zero_lose = []
        one_lose = []
        for key in win_count.keys():
            if key not in lost_count:
                zero_lose.append(key)
        for key, val in lost_count.items():
            if val == 1:
                one_lose.append(key)
        
        return [sorted(zero_lose), sorted(one_lose)]
            
        
        
        