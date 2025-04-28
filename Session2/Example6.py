from colorama import Fore,Back
for i in range (1,9):
    for j in range (1,9):
        if (i+j)%2==0:
            print(Back.WHITE, end="\t")
        else:
            print(Back.BLACK, end="\t")
    print(Back.RESET)