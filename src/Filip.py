num1, num2 = map(str,input().split())

num1rev = list(reversed(num1))
num2rev = list(reversed(num2))

num1final = int("".join(num1rev))
num2final = int("".join(num2rev))

if(num1final>num2final):
    print(num1final)
else:
    print(num2final)
