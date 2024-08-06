input1 = int(input())
count = 0
for i in range(input1):
    input2 = input()
    if "CD" in input2:
        count += 1
print(input1 - count)
