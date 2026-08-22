nums1={2,4,6,7,8,9}
nums2={2,4,6,1,3,5}
#Sets are not in order
print(nums1.union(nums2))
print(nums1.intersection(nums2)) #common
print(nums1.difference(nums2)) #Discard values from nums1 that are present in nums2
print(nums2.difference(nums1)) #different than previous


print(nums2.symmetric_difference(nums1)) #unique elements of both sets 


print({1,2,3,4}.issuperset({1,2,3}))