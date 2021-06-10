def patt(n):
    for i in range(1,n):
        for j in range(i):
            print("*",end="")
        print("\n")
n=int(input("enter the number="))
patt(n)
