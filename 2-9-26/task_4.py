# string = "enigmatix"
# num = 2

# remove = len(string)
# # for i in range(len(string)):
#     # print(string[num: i], end="")

# print(string[num: remove])    


def abc(string, num):
    return string[num: len(string)] 

i = abc("enigmatix", 3)
print(i)
