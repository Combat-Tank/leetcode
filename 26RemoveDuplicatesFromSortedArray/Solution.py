class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 1
        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1]):
                nums[count] = nums[i]
                count = count + 1

        return count

if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([1,1,2])