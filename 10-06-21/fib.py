def fib(n):
    a=0
    b=1
    i=2
    print(f'{a},{b},',end="")
    sum=0
    while(i<n):
        sum=a+b
        print(f'{sum},',end="")
        a=b
        b=sum
        i=i+1
    
n=int(input("enter the number="))
fib(n)
