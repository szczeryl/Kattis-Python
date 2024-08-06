input1 = int(input())

for i in range (input1):
    input2 = input()
    input3 = input() 
    list1= [] 
    
    for j in range (len(input2)):
        if input2[j] != input3[j]: 
            list1.append("*")
        else: 
            list1.append(".")
            
    print(input2)
    print(input3)
    print("".join(list1))
    print()
