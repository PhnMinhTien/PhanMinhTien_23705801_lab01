a=int(input("Nhập số giờ thứ nhất: "))
b=int(input("Nhập số phút thứ nhất: "))
c=int(input("Nhập số giây thứ nhất: "))
x=int(input("Nhập số giờ thứ hai: "))
y=int(input("Nhập số phút thứ hai: "))
z=int(input("Nhập số giây thứ hai: "))
A = a + x
B = b + y
C = c + z
if C >= 60:
    C = C - 60
    B = B + 1
if B >= 60:
    B = B - 60
    A = A + 1
print("Tổng là:", A, "giờ", B, "phút", C, "giây")
if (a < x) or (a == x and b < y) or (a == x and b == y and c < z):
    a, x = x, a
    b, y = y, b
    c, z = z, c
X = a - x
Y = b - y
Z = c - z
if Z < 0:
    Z = Z + 60
    Y = Y - 1
if Y < 0:
    Y = Y + 60
    X = X - 1

print("Hiệu là:", X, "giờ", Y, "phút", Z, "giây")