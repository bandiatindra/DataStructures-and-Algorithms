class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
      
        if not nums:
            return 0
        #This is very important to keep the nums in hash map
        nums = set(nums)
        
        parent = {}
        for num in nums:
            parent[num] = num
        rank = defaultdict(int)        
                
        def Find(i):
            if i != parent[i]:
                parent[i] = Find(parent[i])
            return parent[i]
        
        def Union(i,j):
            i_parent = Find(i)
            j_parent = Find(j)
            if i_parent == j_parent:
                return
            if rank[i_parent] < rank[j_parent]:
                parent[i_parent] = j_parent
            else:
                parent[j_parent] = i_parent
                if rank[i_parent] == rank[j_parent]:
                    rank[i_parent] = rank[i_parent] + 1
            
            
        
        for num in nums:
            if num - 1 not in nums:
                cur = num
                while cur + 1 in nums:
                    Union(cur,cur+1)
                    cur += 1
                    
        cnt = Counter(parent.values())
        max_val = max(cnt.values())    
           
            
        
        return max_val
        