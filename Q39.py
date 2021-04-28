Q1 = int(input(":"))

for i in range(1,Q1,2):
    for o in range(1,Q1,2):
        print(" ", end="")
    print(str(i))

for i in range(1,Q1+2,2): 
    print(str(i),end="")
    
for i in range(1,Q1,2): 
    print(str(Q1-i-1),end="")

print()

for i in range(1,Q1,2):
    for o in range(1,Q1,2):
        print(" ", end="")
    print(str(Q1-i-1))