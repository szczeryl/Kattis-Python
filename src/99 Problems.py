input1 = int(input())
if input1<100:
    print(99)
else:
    smaller = int(str(int(input1/100)-1)+'99')
    bigger = int(str(int(input1/100))+'99')
    if abs(input1-bigger) < abs(input1-smaller):
        print(bigger)
    elif abs(input1-bigger) > abs(input1-smaller):
        print(smaller)
    elif abs(input1-bigger) == abs(input1-smaller):
        print(bigger)
