class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        aux = []
        for i in range(k):
            aux[i] = nums[len(nums)-i]

        for i in range(len(nums),k):
            nums[i] = nums[i-k]
        
        for i in range(k):
            nums[i] = aux[i]
