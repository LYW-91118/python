k = 0
a = list(input("請輸入一串數字"))
b = list(a)
for j in range(len(a)-1):
    for i in range(len(a)-j-1):
        if a[i] > a[i+1] :
            k = a[i]
            a[i] = a[i+1]
            a[i+1] = k
print(a)
for j in range(len(a)-1):
    for i in range(len(a)-j-1):
        if b[i+1] > b[i] :
            k = b[i]
            b[i] = b[i+1]
            b[i+1] = k
print(b)
aa=""
bb=""
for i in a:
    aa += i
for i in b:
    bb += i
ans = int(bb)-int(aa)
print(ans)
