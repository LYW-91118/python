a = [30,60,90,5,77]
b = list("1234")
c = list(input("請輸入你的答案"))

A = 0
B = 0
for i in range(len(b)) :
    for j in range(len(c)) :
        if i == j and b[i] == c[j] :
            A = A + 1
            break
        elif b[i] == c[j] :
            B = B + 1
            break
print(A,"A",B,"B")