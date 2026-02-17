def analyse_name(full_name):
    alphabets = 0
    spaces = 0

    for chr in full_name:
        if chr == " ":
            spaces += 1

        else:
            alphabets +=1   

    name_length_analyse = 0

    if alphabets >= 10:
        name_length_analyse = "Long Name"
    else:
        name_length_analyse = "Short Name" 

    return name_length_analyse


full_name = input("Enter your full name: ")
name_length_analyse = analyse_name(full_name)

print(f"Name Type: {name_length_analyse}")