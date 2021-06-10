def fact(n):
    sum=1
    i=1
    while(i<=n):
        sum=sum*i
        i=i+1
    return sum
n=int(input("enter the number="))
print("factorial is=",fact(n))
