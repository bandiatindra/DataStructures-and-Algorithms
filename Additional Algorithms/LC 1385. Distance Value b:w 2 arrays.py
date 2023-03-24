class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        # Below is O(n*m) time.  
        # cnt = {}
        
        # for i in range(len(arr1)):
        #     for j in range(len(arr2)):
        #         if abs(arr1[i] - arr2[j]) <= d:
        #             cnt[i] = 0
        #             break
        #         else:
        #             cnt[i] =1
            

        # return sum(cnt.values())

        # Let's try to write in O(nlogn) via Binary Search. The idea is if we find any value b/w arr1[i] +/- d in arr2 then return 0. Else, we are good!
        #arr1.sort()
        arr2.sort()

        def binary_search(arr,lower,higher):
            r = len(arr) -1
            l = 0
            
            if r >= 0:
                mid = (l+r)//2
                if arr[mid] == higher or arr[mid] == lower:
                    return 0
                if arr[mid] < higher and arr[mid] > lower:
                    return 0
                if arr[mid] > higher:
                    return binary_search(arr[:mid],lower,higher)
            
                if arr[mid] < lower:
                    return binary_search(arr[mid+1:],lower,higher)
            
            return 1
            
        cnt = 0
        for i in range(len(arr1)):
            higher = arr1[i] + d
            lower = arr1[i] - d 
            cnt = cnt + (binary_search(arr2,lower,higher))
        return cnt

            

