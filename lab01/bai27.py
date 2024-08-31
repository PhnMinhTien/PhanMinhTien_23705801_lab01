a=(input("Nhập loại hình(hình vuông, hình chữ nhật, hình tròn):"))
if a=="hình chữ nhật":
  A = float(input("Nhập chiều dài:"))
  B = float(input("Nhập chiều rộng:"))
  print("Diện tích hình chữ nhật là:",A*B)
  print("Chu vi hình chữ nhật là:",(A+B)*2)
elif a=="hình tròn":
  C=float(input("Nhập bán kính:"))
  print("Diện tích hình tròn là:",C*C*3.14)
  print("Chu vi hình tròn là:",C*2*3.14)
elif a=="hình vuông":
  E=float(input("Nhập chiều dài:"))
  print("Diện tích hình vuông là:",E*E)
  print("Chu vi hình vuông là:",E*4)
else:
  print("Chỉ nhập 1 trong 3 loại hình trên")
