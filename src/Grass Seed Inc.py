input1 = float(input())
input2 = int(input())
area = 0
for i in range(input2):
    input3 = input() 
    inp = input3.split(" ")
    a,b = float(inp[0]), float(inp[1])
    area += a * b 
ans = area * input1 
newans = round(ans, 8)
print(newans)
