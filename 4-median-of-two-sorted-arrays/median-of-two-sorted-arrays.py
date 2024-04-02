class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newlist = []
        i = 0
        j = 0
        while (i < len(nums1) or j < len(nums2)):
            if i >= len(nums1):
                newlist.append(nums2[j])
                j+=1                
            elif j >= len(nums2):
                newlist.append(nums1[i])
                i+=1
            elif(nums1[i] < nums2[j]):
                newlist.append(nums1[i])
                i+=1
            else:
                newlist.append(nums2[j])
                j+=1
        
        print(newlist)
        if(len(newlist)%2 == 0):
            l = newlist[len(newlist)//2-1]
            r = newlist[len(newlist)//2]
            #print(str(l) + " " + str(r))
            return ((l+r)/2.0)
        else:
            #print(len(newlist)//2)
            return newlist[len(newlist)//2]
