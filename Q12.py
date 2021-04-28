num = input("輸入一整數序列：")

s = num.split()

sum = len(s)

a = 0

for i in range(sum):
    if(s.count(s[i]) >= (sum/2)):
        print("過半元素為：%s" %(s[i]))
        a = 1
        break

if(a == 0 ):
    print("no")