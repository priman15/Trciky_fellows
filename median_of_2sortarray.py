#Using Binary search method. Time Complexity:O(min(log m, log n)) because we skip one half of the array in each step.
#Binary search to find a point in two lists such that all the elements on the left hand side of the point are lesser than all the elements on the right side of the point.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1)<=len(nums2)):
            x=len(nums1)
            y=len(nums2)
        else:
            return self.findMedianSortedArrays(nums2,nums1)
        low=0
        high=x
        
        while(low<=high):
            partitionX=int((low+high)/2)
            partitionY=int((x+y+1)/2-partitionX)
            maxleftX=-999999999999999999999 if (partitionX==0) else nums1[partitionX-1]
            maxrightX=999999999999999999999 if (partitionX==x) else nums1[partitionX]
            maxleftY=-99999999999999999999 if (partitionY==0) else nums2[partitionY-1]
            maxrightY=99999999999999999999 if (partitionY==y) else nums2[partitionY]
            if(maxleftX<=maxrightY and maxleftY<=maxrightX):
                if((x+y)%2==0):
                    return((max(maxleftY,maxleftX)+min(maxrightX,maxrightY))/2)
                else:
                    return(max(maxleftY,maxleftX))
            elif(maxleftX>maxrightY):
                high=partitionX-1
            else:
                low=partitionX+1
