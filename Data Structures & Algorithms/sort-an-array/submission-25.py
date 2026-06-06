class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # def merge(arr, low, mid, high):
        #     tmp = []
        #     i1, i2 = low, mid + 1

        #     while i1 <= mid and i2 <= high:
        #         if arr[i1] < arr[i2]:
        #             tmp.append(arr[i1])
        #             i1 += 1
        #         else:
        #             tmp.append(arr[i2])
        #             i2 += 1

        #     while i1 <= mid:
        #         tmp.append(arr[i1])
        #         i1 += 1

        #     while i2 <= high:
        #         tmp.append(arr[i2])
        #         i2 += 1

        #     for i in range(low, high + 1):
        #         arr[i] = tmp[i-low]

        # def mergesort(arr, low, high):
        #     if low >= high:
        #         return
                
        #     mid = (low + high) // 2
        #     mergesort(arr, low, mid)
        #     mergesort(arr, mid + 1, high)
        #     merge(arr, low, mid, high)

        # mergesort(nums, 0, len(nums) - 1)
        # return nums

        def partition(arr, low, high):
            mid = (low + high) // 2
            arr[low], arr[mid] = arr[mid], arr[low]
            i = low
            j = high

            while i < j:
                while i < high and arr[i] <= arr[low]:
                    i += 1

                while j > low and arr[j] > arr[low]:
                    j -= 1

                if i < j:
                    arr[i], arr[j] = arr[j], arr[i]

            arr[low], arr[j] = arr[j], arr[low]
            return j


        def quicksort(arr, low, high):
            if low < high:
                p = partition(arr, low, high)

                quicksort(arr, low, p - 1)
                quicksort(arr, p + 1, high)

        quicksort(nums, 0, len(nums) - 1)
        return nums

        
                