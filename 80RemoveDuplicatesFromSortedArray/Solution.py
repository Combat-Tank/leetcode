class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 1
        currentElementCount = 1
        if(len(nums) <= 3):
            return len(nums)
        
        for i in range(1, len(nums)):
            if(nums[i] != nums[i-1]):
                nums[count] = nums[i]
                count += 1
                currentElementCount = 0
                print(nums)
            elif(currentElementCount < 2):
                nums[count] = nums[i]
                count += 1
                
            currentElementCount += 1
            print(nums)
            
        return count

if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,4,6,8,8,8])