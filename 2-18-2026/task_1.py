# 📅 DAY 6 – New Task
# 🔥 Frequency Counter (Without dict)

nums = [1,2,1,3,2,1,4]

new = []

for i in nums:
    if i not in new:
        count = nums.count(i)
        print(f"{i} = {count}")
        new.append(i)