class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Based on Moore's Voting Algorithm
        """
        size = len(nums)
        maj_candidate_idx = 0
        count = 1
        for i in range(0,size):
            if(nums[i] == nums[maj_candidate_idx]):
                count += 1
            elif(count == 0):
                maj_candidate_idx = i
                count = 1
            else:            
                count -=1
            
            if(count >= (size/2)):
                print(nums[maj_candidate_idx])
                return nums[maj_candidate_idx]


        return 0

if __name__ == "__main__":
    s = Solution()
    s.majorityElement([2,2,1,1,1,2,2])