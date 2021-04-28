k = float(input("請輸入路程公里數(km)"))
if( k <= 1.5):
    print("所需車資：75元")
elif( k >1.5 ):
    k_1 = ((k-1.5)/0.25)
    k_2 = (math.ceil(k_1))*5
    kt = 75+k_2
    kt = ('%.0f'%kt)
    print("所需車資：%s元"%(kt))