nums = [1,2,3,4,5]

reverse_list = []

length = len(nums)

for i in range(length - 1, -1, -1):
    # reverse_list += [nums[i]]
    reverse_list.append(nums[i])
    
print(f"New List: {reverse_list}")


# for i in reversed(nums):
#     print(i, end=" ")

# for i in nums[::-1]:
#     print(i, end=" ")

