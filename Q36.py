n = int(input("0<n<1000000"))
while n != 1:
    if(n%2==1):
        n = n*3+1
    else:
        n = n/2
    print(int(n))