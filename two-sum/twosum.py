#!/usr/bin/python


#--------------------------------------------------------------
#
# Time complexity O(n)
# Because there is only loop iteration and using the magic of dictionary
# you can lookup values inside.
#
#--------------------------------------------------------------

def calculate(nums):

  data={}                                 # declare empty dict
  for index, value in enumerate(nums):    # loop over elements and use enumerate to index values
    if target - value in data:            # if result of target and value exist in data do the following
      print target, value, target-value, data[target-value]
      print ([data[target-value]])
      return [data[target-value], index]  # if value is found then return value,index
    else:                                 # else if result of target and value does not exist,
      data[value] = index                 # add value,index to data



    
nums=[2,7,11,15]                 # list index: 0,1,2,3
target=9                              
calculate(nums)                  # output should be: [0,1]

nums=[3,2,4]                     # list index: 0,1,2   
target=6      
calculate(nums)                  # output should be: [1,2]

nums=[3,3]                       # list index: 0,1
target=6      
calculate(nums)                  # output should be: [0,1]
