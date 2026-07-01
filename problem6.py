i=int(input("Enter the number: "))
n=0

while i>0:
    j=i%10
    n=n*10+j
    i=i//10

print(n)