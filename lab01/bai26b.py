n = input("Nhập số nguyên N có 4 chữ số: ")
a = n[0]
b = n[1]
c = n[2]
d = n[3]

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if a > d:
    a, d = d, a
if b > c:
    b, c = c, b
if b > d:
    b, d = d, b
if c > d:
    c, d = d, c

print("Số có các chữ số theo thứ tự tăng dần là:", a + b + c + d)