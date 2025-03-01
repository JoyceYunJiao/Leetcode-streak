class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #loop through all the elements in nums
        #store element as pair of counts and element by using hashmap 
        #increase the count by 1 each time 
        #keep the maximum count and check if count > n/2 

        #create a dictionary
        elements = {}
        #elements[num[i]]

        #loop through nums and add the count for each element 
        for num in nums:
            # Increment the count for the current element
            elements[num] = elements.get(num, 0) + 1

            #check if the count is bigger than n/2 
            if elements[num] > len(nums)/2:
                return num

