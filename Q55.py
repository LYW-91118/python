in2 = int(input("請輸入正整數"))
maths = 0
maths3 = 0
t = 1
n = 0
for  maths in range(1,in2+1):
    n = 0
    for maths3 in range(1,maths+1):
        n = n+1
        t = maths*n
        print(t,end=" ")
    print()