input1 = int(input())
if input1 == 0: 
    print("++")
    print("++")
else: 
    print("+" + "-"*input1 + "+")
    for i in range (input1):
        print ("|" + " "* input1 + "|")
    print("+" + "-"*input1 + "+")