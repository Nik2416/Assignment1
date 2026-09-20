n=1234
num=n
res=0

while num>0:
  last_dig=num%10
  res=(res*10)+last_dig
  num=num//10

print("this is the reverse of the number 1234",res)
if (n==res):
  print("This ia a palindrome number")
else:
  print("this is not a palindrome number")
