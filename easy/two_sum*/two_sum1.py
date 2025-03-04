class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # this is a brute force solution for this question 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)): 
        #         if nums[i] + nums[j] == target: 
        #             return i, j
        # a better solution is to use hashmap to store the number and index as a pair
        # check if the complment is in the hashmap 

        # Create an empty hashmap to store each number and its corresponding index
        num_index = {}

        # Store number and index as a pair in hashmap
        # While check if the complement appeared in the hashmap 
        for i in range(len(nums)):
            # Calculate the complement 
            complement = target - nums[i]

             # If the complement exists in the hashmap, we found a valid pair
            if complement in num_index:
                return i, num_index[complement]

            # Otherwise, store the current number with its index in the hashmap
            num_index[nums[i]] = i

