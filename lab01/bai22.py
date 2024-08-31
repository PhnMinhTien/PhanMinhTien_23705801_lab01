a=float(input("Nhập a:"))
b=float(input("Nhập b:"))
print("Ta có phương trình: ",a,"x + ",b," = 0")
if a!=0:
      print("Phương trình có 1 nghiệm",-b/a)
elif a==0 and b==0:
      print("Phương trình có vô số nghiệm")
elif a==0 and b!=0:
      print("Phương trình vô nghiệm")
