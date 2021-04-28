m = float(input())
if( m <= 120):
    m1 = m*2.1
    m1 = ('%.2f'%m1)
    print(m1)
    print("summer months:%s" %(m1))
    print("Non-summer months:%s" %(m1))
elif(m>=121 and m<=330):
    m2 = (m-120)*3.02+252
    m22 = (m-120)*2.68+252
    m2 = ('%.2f'%m2)
    m22 = ('%.2f'%m22)
    print("summer months:%s" %(m2))
    print("Non-summer months:%s" %(m22))
elif(m>=331 and m<=500):
    m2 = (m-330)*4.39+252+634.2
    m22 = (m-330)*3.61+252+562.8
    m2 = ('%.2f'%m2)
    m22 = ('%.2f'%m22)
    print("summer months:%s" %(m2))
    print("Non-summer months:%s" %(m22))
elif(m>=501 and m<=700):
    m2 = (m-500)*4.97+252+634.2+746.3
    m22 = (m-500)*4.01+252+562.8+613.7
    m2 = ('%.2f'%m2)
    m22 = ('%.2f'%m22)
    print("summer months:%s" %(m2))
    print("Non-summer months:%s" %(m22))
elif(m>=701):
    m2 = (m-700)*4.97+252+634.2+746.3+994
    m22 = (m-700)*4.01+252+562.8+613.7+802
    m2 = ('%.2f'%m2)
    m22 = ('%.2f'%m22)
    print("summer months:%s" %(m2))
    print("Non-summer months:%s" %(m22))