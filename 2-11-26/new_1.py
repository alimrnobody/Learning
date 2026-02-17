nums = [4,7,2,4,9,2,1,4,7,8]

check_num = 0
even = 0

for i in nums:
    if i == 4:
        check_num += 1
    if i % 2 == 0:
        even += 1

print(f"Total 4 in list: {check_num}")    
print(f"Total Even in list: {even}", end="")    
