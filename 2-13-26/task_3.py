nums = [1,2,3,2,4,5,1,6,3]

duplicates_list = []

for i in nums:
    if i not in duplicates_list:
        duplicates_list.append(i)

print(duplicates_list)        