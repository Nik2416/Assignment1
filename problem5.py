n=int(input("Enter the number: "))
term=2
sum=0

for i in range(n):
   sum+=term
   term=term*10+2

print(sum)