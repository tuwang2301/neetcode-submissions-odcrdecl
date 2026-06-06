class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr, low, mid, high):
            tmp = []
            i1, i2 = low, mid + 1

            while i1 <= mid and i2 <= high:
                if arr[i1] < arr[i2]:
                    tmp.append(arr[i1])
                    i1 += 1
                else:
                    tmp.append(arr[i2])
                    i2 += 1

            while i1 <= mid:
                tmp.append(arr[i1])
                i1 += 1

            while i2 <= high:
                tmp.append(arr[i2])
                i2 += 1

            for i in range(low, high + 1):
                arr[i] = tmp[i-low]

        def mergesort(arr, low, high):
            if low >= high:
                return
                
            mid = (low + high) // 2
            mergesort(arr, low, mid)
            mergesort(arr, mid + 1, high)
            merge(arr, low, mid, high)

        mergesort(nums, 0, len(nums) - 1)
        return nums
                