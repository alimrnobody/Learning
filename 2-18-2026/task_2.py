# 🔥 Next Task (Manual Frequency – No count())

nums = [1,2,1,3,2,1,4]
count = []
value = 0

for i in nums:
    if i not in count:
        value = 0

        for j in nums:
            if j == i:
                value += 1
    
        count.append(i)
        print(f"{i} : {value}")
    