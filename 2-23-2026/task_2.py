nums = [3,5,3,7,9,5,1]
new = []

for i in nums:
    count = 0 
    for j in nums:
        if i == j:
            count += 1 
    if count == 1:
        new.append(i)

smallest = new[0]
for q in new:
    if q < smallest:
        smallest = q

print(smallest)        
