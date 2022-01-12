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
    diff = target - value                 # assign result of target - value to diff

    # if diff exist in data dict return key,value initially data will be empty in data 
    # but we will add to it in else statement. Added format is key=value, value=index
    # so its technically reversed when you reference data using key you get index as output.

    if diff in data:                      
      return [data[diff], index]          # if value is found then return value,index
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

