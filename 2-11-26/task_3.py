num = [45, 2, 89, 12, 7]

maximum = num[0]
minimum = num[0]

for i in num:
    if i > maximum:
        maximum = i
    elif i < minimum:
        minimum = i    

print(f"Maximum Num: {maximum}")
print(f"Minimum Num: {minimum}")