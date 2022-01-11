#!/usr/bin/python


#--------------------------------------------------------------
#
# Time complexity O(n^2)
# Because there are two loops this is not most opitmal solution 
#
#--------------------------------------------------------------

#nums=[2,7,11,15]                  # index: 0,1,2,3
#target=9                          # target variable
nums=[3,2,4]
target=6


for i in range(len(nums)):        # loop over length of nums array starting with index 0
  for x in range(1,len(nums)):    # loop over length of nums array starting with index 1
    p=nums[i]+nums[x]             # add index elements together

    l=[]                          # declare empty array list
    if p == target:               # compare two added indexes against target
      l.append(i)                   # append i index to l list array
      l.append(x)                   # append x index to l list array
      l=str(l).replace(' ','')    # remove space between array list elements
      print (l)                   # print l list array

