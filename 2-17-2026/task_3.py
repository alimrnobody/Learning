nums = [1,2,1,3,2,1,4]

new1 = []

new2 = []

for i in nums:
    if i not in new1:
        new1.append(i)

# for i in nums.count(new2):
#     new2.append(i)
#     print(f"{i} = {new2}")



print(new1)