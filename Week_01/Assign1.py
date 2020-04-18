"""
删除排序数组中的重复项
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number=0
        cur=1
        for i,num in enumerate(nums):
            if num!=nums[cur-1]:
                nums[cur]=num
                cur+=1
        return cur