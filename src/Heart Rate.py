input1 = int(input())
for i in range (input1):
    input2 = input() 
    inp = input2.split()
    b,p = int(inp[0]), float(inp[1])
    actual = 60 * b / p
    offset = 60 / p
    min, max = "{0:.4f}".format(actual - offset), "{0:.4f}".format(actual + offset)
    actual = "{0:.4f}".format(actual)
    print(min+ " " + str(actual)+ " "+ max)
