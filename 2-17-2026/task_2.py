nums = [34,1,12,2,89,5,67,90,]

maximum = nums[0]
minimum = nums[0]

for i in nums:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i   


print(maximum)        
print(minimum)        