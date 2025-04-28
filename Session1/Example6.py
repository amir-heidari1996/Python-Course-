age=int(input("how old are you?"))
if 0<age<7:
    print("baby")
elif 7<=age<12:
    print("child")
elif 12<=age<18:
    print("teenager")
elif 18<=age<40:
    print("young")
elif 40<=age<60:
    print("middle age")
elif 60<=age:
    print("old")
else:
    print("invalid age")
    