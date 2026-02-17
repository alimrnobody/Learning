num1 = 20
num2 = 30

def abc(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
    
print(abc(num1, num2))    