"""
旋转数组
https://leetcode-cn.com/problems/rotate-array
"""

class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        times=0
        i=0
        while times<len(nums):
            cur=(i+k)%len(nums)
            prev=nums[i]
            while cur!=i:
                prev,nums[cur]=nums[cur],prev
                times+=1
                cur=(cur+k)%len(nums)
            nums[cur]=prev
            times+=1
            i+=1
        return nums


class Solution2(object):
    def rotate(self,nums,k):
        k=k%len(nums)
        nums.reverse()
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
        return nums