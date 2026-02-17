nums = [1,2,3,2,4,0,5,1,6,3]

previous_num = []

new_list = []

for i in nums:
    if i in previous_num and i not in new_list:
        new_list.append(i)
    previous_num.append(i)
   
print(new_list)



# 2nd Method
nums = [1,2,3,2,4,5,1,6,3] 

new_list = [] 

for i in nums: 
    if nums.count(i) > 1 and i not in new_list: 
        new_list.append(i) 
        
print(new_list)