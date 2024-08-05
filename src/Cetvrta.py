input1, input2, input3 = input(), input(), input()
inp1, inp2, inp3 = input1.split(" "), input2.split(" "), input3.split(" ")
a,b = int(inp1[0]), int(inp1[1])
c,d = int(inp2[0]), int(inp2[1])
e,f = int(inp3[0]), int(inp3[1])
ans1, ans2 = 0,0
if a == c: 
    ans1 += e 
if a == e: 
    ans1 += c
if c==e: 
    ans1 += a
if b==d: 
    ans2 += f
if d==f: 
    ans2 += b
if b==f: 
    ans2 += d
