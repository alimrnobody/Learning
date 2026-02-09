# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if num1 * num2 <= 1000:
#     print(f"The product of {num1} and {num2} is {num1 * num2}.")
# else:
#     print(f"The sum of {num1} and {num2} is {num1 + num2}.")   


def abc(num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2   

i = abc(10, 200)
print(i)