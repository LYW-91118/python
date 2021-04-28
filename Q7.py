m = float(input("輸入月租費型式"))
t = float(input("輸入通話時間"))
if(m == 186):
    t = t*0.09
    if(t>m):
        t = t*0.8
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))
    elif(t<m):
        t = t*0.9
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))
elif(m == 386):
    t = t*0.08
    if(t>m):
        t = t*0.7
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))
    elif(t<m):
        t = t*0.8
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))
elif(m == 586):
    t = t*0.07
    if(t>m):
        t = t*0.6
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))
    elif(t<m):
        t = t*0.7
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))
elif(m == 986):
    t = t*0.06
    if(t>m):
        t = t*0.5
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))
    elif(t<m):
        t = t*0.6
        t = ('%.0f'%t)
        print("通話費為：%s"%(t))