input1 = str(input())
length = len(input1)
p = length//2
if length %2 ==0:
    if input1[p-1] == "(" and input1[p] == ")":
        print("correct")
    else: 
        print("fix")
else: 
    print("fix") 
