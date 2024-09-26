import math
try:
 r=float(input("Mời bạn nhập bán kính hình tròn:"))
 cv=2*math.pi*r
 dt=r**2*math.pi
 formatcv= format(cv,".2f")
 print("Chu vi = ",formatcv)
 print("Diện tích=",dt)
except:
 print("Lỗi rồi!")
