num1_in_str = input("Enter your num: ")
num2_in_str = input("Enter your num: ")
operator = input("Enter the operator")

num1 = int(num1_in_str)
num2 = int(num2_in_str)

if operator == "+":
    print("Result: ", num1 + num2)

elif operator == "*":
    print("Result: ", num1 * num2)    

elif operator == "-":
    print("Result: ", num1 - num2)    

elif operator == "/":
    print("Result: ", num1 / num2)    