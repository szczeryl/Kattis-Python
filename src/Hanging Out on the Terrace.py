input1 = input()
inp1 = input1.split()
a,b = int(inp1[0]), int(inp1[1])
count, ans =0,0
for i in range(b): 
    input2 = input() 
    inp2 = input2.split()
    if inp2[0] == "enter":
        temp = count + int(inp2[1])
        if a>= temp:
            count += int(inp2[1])
        else:
            ans += 1
    else: 
        count -= int(inp2[1])
print(ans) 
