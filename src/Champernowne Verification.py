input1 = input()
ans, i = "",1
while i in range (len(input1)+1):
    ans += str(i)
    i+= 1
if input1 == ans: 
    print(input1[i-2])
else: 
    print (-1)
