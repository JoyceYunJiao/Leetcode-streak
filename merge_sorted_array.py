class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        I use the two walking algorithm but backwards, I started at the    last index of the two arrays and compare them 
        I added the larger element to the last avaialble index of num1, I keep adding elements to the end of the array while 
        """

        #end of list1
        index_1 = m-1
        #end of list2
        index_2 = n-1
        #the place to insert large element
        #starting from the end of the list
        index_3 = m+n-1


        while index_3 >= 0:

            while index_1 >= 0 and index_2 >= 0 :
                if nums1[index_1] <= nums2[index_2]:
                    nums1[index_3] = nums2[index_2]
                    index_3 -= 1
                    index_2 -= 1
                    
                else:
                    nums1[index_3] = nums1[index_1]
                    index_3 -= 1
                    index_1 -= 1

            #edge case 
            if index_1 < 0:
                nums1[index_3] = nums2[index_2]
                index_3 -= 1
                index_2 -= 1

            elif index_2 < 0:
                nums1[index_3] = nums1[index_1]
                index_3 -= 1
                index_1 -= 1

        

