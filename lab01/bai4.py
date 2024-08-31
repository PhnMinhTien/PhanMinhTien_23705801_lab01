a=int(input("Nhập vào số nguyên dương a  có 2 chứ số:"))
if  a < 10 or a > 99:
  print("Số không phù hợp")
else:
  print("Tổng 2 chữ số của số nguyên dương a là:" ,a//10+a%10)