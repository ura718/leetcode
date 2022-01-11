#!/usr/bin/python


#--------------------------------------------------------------
#
# Time complexity O(n)
# Because there is only loop iteration and using the magic of dictionary
# you can lookup values inside.
#
#--------------------------------------------------------------


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:

    data = {}                                 # declare empty dict
    for index, value in enumerate(nums):    # loop over elements and use enumerate to index values
      diff = target - value
      if diff in data:                      # if result of diff exist in data do the following
        return [data[diff], index]          # return value,index
      data[value] = index                   # add value,index to data
