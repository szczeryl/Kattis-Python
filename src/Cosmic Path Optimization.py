input1 = int(input())
input2 = input()
total = 0
inp= input2.split(" ")
for i in range(input1):
    total += int(inp[i])
ans = ((int(total)/input1)//1)
print(int(ans))
