nums = [3,5,3,7,9,5,1]
smallest = None

for i in nums:
    count = 0 
    for j in nums:
        if i == j:
            count += 1
    if count == 1:
        if smallest is None: 
            smallest = i
        elif i < smallest:
            smallest = i
print(smallest)            