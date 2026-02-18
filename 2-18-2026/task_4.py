# 🔥 Next Task (String Frequency – Slight Upgrade)

text = "banana"

check_count = []
value = 0

for i in text.lower():
    if i not in check_count:
        value = 0
        for j in text.lower():
            if j == i:
                value += 1

        check_count.append(i)
        print(f"{i} : {value}")        