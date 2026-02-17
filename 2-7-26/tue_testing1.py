# string = input("Enter any string: ")

# length = len(string)

# for i in (string):
#     if i % 2 == 0:
#         print(string[i])


word = input("Enter word: ")
print("Original String:", word)

print("Printing only even index chars")

for i in range(0, len(word), 2):
    print(word[i])
