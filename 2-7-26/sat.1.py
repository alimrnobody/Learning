def analyse_number(number_str):
    digits = 0
    zeros = 0
    i = 0

    while i < len(number_str):
        char = number_str[i]

        if char.isdigit():
          digits += 1
        if char == "0":
             zeros += 1
             
        i += 1

        

    number_type = 0

    if digits >= 5 and zeros >= 1:
        number_type = "Valid Number" 
    else:
        number_type = "Invalid Number"

    return number_type

number_str = input("Enter a Number: ")
number_type = analyse_number(number_str)

print(f"Number Status: {number_type}")


