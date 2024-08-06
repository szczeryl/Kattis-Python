input1 = input()
j = ""
found_a = False

for i in range(len(input1)):
    if input1[i] == "a" and not found_a:
        j = (input1[i::])
        found_a = True
print(j)
