a=0
b=1
c=int(input('limit'))
print(a ,end=" ")
print(b ,end=" ")
for i in range(c):
  tem=a+b
  a=b
  b=tem
  print(tem)