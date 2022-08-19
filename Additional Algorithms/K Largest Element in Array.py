class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
                
        # Sift Down Function
        def SiftDown(min_heap, i):
            
            size = len(min_heap)
            max_index = i
            left_index  = 2*i+1
            right_index = 2*i+2

            if left_index < size and min_heap[left_index] < min_heap[max_index]:
                max_index = left_index

            if right_index < size and min_heap[right_index] < min_heap[max_index]:
                max_index = right_index

            if i != max_index:
                temp = min_heap[i]
                min_heap[i] = min_heap[max_index]
                min_heap[max_index] = temp           
                SiftDown(min_heap, max_index)
                  
       # Create heap
        def heap_create(min_heap):
            size = len(min_heap)
            for i in range(int(size/2)-1,-1,-1):
                SiftDown(min_heap, i)
                       
        min_heap = []
        for i in range (k):
            min_heap.append(nums[i])
        
        heap_create(min_heap)
                    
        for i in range(k, len(nums)):
            if min_heap[0] > nums[i]:
                continue
            else:
                min_heap[0]= nums[i]
                SiftDown(min_heap,0)
        
        return min_heap[0]