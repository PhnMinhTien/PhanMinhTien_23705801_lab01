d=int(input("Nhập biển số xe của bạn(gồm 4 chữ số):"))
a=d//1000
b=(d%1000)//100 
c=((d%1000)//10)%10
e=(d%1000)%100%10
x=a+b+c+e
A=x//10
B=x%10
Y=A+B
print("Tổng nút của bạn là:",x,  "vậy số nút là:",Y )
    