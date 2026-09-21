#printprime numbers in an interval

b=int(input('Enter a number'))
c=int(input('Enter a number'))

for i in range (b,c+1):
  if(i>1):
    for j in range(2,i):
      if(i%j==0):
       break
    else:print(i)