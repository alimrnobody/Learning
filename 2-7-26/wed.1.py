def analyse_name(full_name):
    alphabets = 0
    spaces = 0

    for chr in full_name:
        if chr == " ":
            spaces += 1

        else:
            alphabets +=1    

    return alphabets, spaces


full_name = input("Enter your full name: ")
alphabets, spaces = analyse_name(full_name)

print(f"Total Alphabets: {alphabets}")
print(f"Total Spaces: {spaces}")