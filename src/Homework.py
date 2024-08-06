input1 = input()
count = 0
if ";" in input1: 
    inp1 = input1.split(";")
    for i in range(len(inp1)):
        if "-" in inp1[i]: 
            inp2 = inp1[i].split("-")
            count += int(inp2[1]) - int(inp2[0]) +1
        else: 
            count += 1
elif ";" not in input1 and "-" not in input1: 
    count =1
else: 
    inp3 = input1.split("-")
    count += int(inp3[1]) - int(inp3[0]) +1
    
print(count)
