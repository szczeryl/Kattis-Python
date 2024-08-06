input = input()
x = input.split( )
for i in range (1, int(x[-1])+1):
    if i% int(x[0])!=0 and i % int(x[1])!= 0:
        print (i)
    elif i% int(x[0]) == 0 and i% int(x[1])!=0: 
        print ("Fizz")
    elif i % int(x[1]) == 0 and i% int(x[0])!=0:
        print ("Buzz")
    elif i % int(x[0])==0 and i % int(x[1]) ==0:
        print ("FizzBuzz")
