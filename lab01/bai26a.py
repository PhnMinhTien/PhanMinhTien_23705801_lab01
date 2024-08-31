a=int(input("Nhập số N:"))
b=int(input("Nhập số M:"))
c=int(input("Nhập số P:"))
if a>b:
      a, b=b,a
if a>c:
      a, c=c,a
if b>c:
      b, c=c,b
print("Theo thứ tự tăng dần" ,a,b,c)