num = [4,7,2,4,9,2,1,4,7,8]

even = 0

for i in num:
    if (i & 1) == 0:
        even += 1

print(even)    