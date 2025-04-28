weight=float(input("what is your weight?"))
height=float(input("what is your height?"))
bmi=weight/(height**2)
if bmi<18:
    print("under weight")
elif 18<=bmi<24.9:
    print ("ideal")
elif 24.9<=bmi<29.9:
    print ("over weight")
elif 29.9<=bmi<34.9:
    print ("fat type1")
elif 34.9<=bmi:
    print ("fat type2")
else:
    print("incorrect input")