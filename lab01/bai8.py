d=float(input("Nhập cân nặng của bạn(kg):"))
c=float(input("Nhập chiều cao của bạn(m):"))
d=d/(c*c)
print("Chỉ số BMI của bạn là:", d)
if d < 18.5:
  print("Phân loại: Thiếu cân")
elif 18.5 <= d < 24.9:
  print("Phân loại: Bình thường")
elif 25.0 <= d < 29.9:
  print("Phân loại: Thừa cân")
elif 30.0 <= d < 34.9:
  print("Phân loại: Béo phì cấp độ 1")
elif 35.0 <= d < 39.9:
  print("Phân loại: Béo phì cấp độ 2")
else:
  print("Phân loại: Béo phì cấp độ 3")