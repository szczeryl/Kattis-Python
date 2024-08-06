list1= ["A","a","E","e","I","i","O","o","U","u"]
input1 = str(input()) 
count = 0 
for i in range(len(input1)):
    if input1[i] in list1: 
        count += 1
print(count)
