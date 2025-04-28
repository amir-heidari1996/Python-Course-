from colorama import Fore
for i in range (1,11):
    for j in range (1,11):
        if i==j or i+j==11:
            print(Fore.RED+str(i*j), end="\t")
        else:
            print(Fore.BLUE+str(i*j), end="\t")
    print()