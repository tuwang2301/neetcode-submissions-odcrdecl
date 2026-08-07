class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i1, i2 = 0, 0
        res = []

        s1 = nums1[:len(nums1) - len(nums2)]
        s2 = nums2

        while i1 < len(s1) and i2 < len(s2):
            if s1[i1] < s2[i2]:
                res.append(s1[i1])
                i1 += 1
            else:
                res.append(s2[i2])
                i2 += 1

        if i1 < len(s1):
            for n in s1[i1:]:
                res.append(n)

        if i2 < len(s2):
            for n in s2[i2:]:
                res.append(n)

        for i, r in enumerate(res):
            nums1[i] = r

