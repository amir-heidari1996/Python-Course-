a=int(input("number1"))
b=int(input("number2"))
s=input("select between -,+,*,/ ")
if s=="*":
    print(a*b)
elif s=="/":
    print(a/b)
elif s=="+":
    print(a+b)
elif s=="-":
    print(a-b)
else:
    print("invalid")
    