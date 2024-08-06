input1 = int(input())
for i in range(input1): 
    input2 = input()
    inp = input2.split(" ") 
    count = int(inp[1])
    for i in range (int(inp[1])+1):
        count += i 
    print(inp[0]+" "+str(count))
