T = int(input("T:"))
FF = int(1)
A1 = int(0)
for i in range(0,T):
    Q1 = int(input("F:"))
    if (Q1-FF)>0:
        A1 = A1+(Q1-FF)*20
    elif (Q1-FF)<0:
        A1 = A1+(Q1-FF)*-10
    FF =Q1
print(str(A1),"元")