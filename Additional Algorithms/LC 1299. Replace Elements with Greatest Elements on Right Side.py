class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max_right = arr[0]

        for i in range (len(arr)-1):
            if arr[i] == max_right:

                max_right = max(arr[i+1:])
                arr[i] = max_right
            else:
                arr[i] = max_right
        arr[-1] = -1
        return arr
        