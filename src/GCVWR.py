input1 = input()
inp = input1.split()
G,T,N = int(inp[0]), int(inp[1]), int(inp[2])
input2 = input()
inp2 = input2.split()
weight = 0
for i in range(N):
    weight += int(inp2[i])
total = 0.9 * (G-T)
print(int(total-weight))
