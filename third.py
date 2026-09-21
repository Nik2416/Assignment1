a=199
b=77
print("before",a)
print(b)
c=b
b=a
a=c

a,b=b,a
print("After",a)
print(b)