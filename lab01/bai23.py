a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
c=float(input("Nhập c:"))
print("Ta có phương trình: ",a,"x^2 + ",b,"x +",c,"=0")
A=b**2-4*a*c
if A>0:
  print("Phương trình có 2 nghiệm phân biệt","x1=",(-b+A**(1/2))/(2*a),"; x2=",(-b-A**(1/2))/(2*a))
elif A==0:
  print("Phương trình có nghiệm kép","x1=x2=",(-b/(2*a)))
elif A<0:
  print("Phương trình vô nghiệm")