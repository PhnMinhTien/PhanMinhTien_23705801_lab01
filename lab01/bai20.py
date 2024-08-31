a=int(input("Nhập số nguyên thứ nhất:"))
b=int(input("Nhập số nguyên thứ hai:"))
c=int(input("Nhập số nguyên thứ ba:"))
d=int(input("Nhập số nguyên thứ tư:"))
lon_nhat = a
if b > lon_nhat:
       lon_nhat = b
if c > lon_nhat:
       lon_nhat = c

print("Số lớn nhất là:", lon_nhat)