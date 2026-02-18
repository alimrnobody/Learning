# 🔥 Next Task (String Traversal – Week 1)

text = "programming"
vowels = "aeiou"
total_vowels = 0

for i in text.lower():
    if i in vowels:
        total_vowels += 1

print(f"Total Vowels: {total_vowels}")
