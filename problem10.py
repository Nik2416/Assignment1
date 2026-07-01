vowels=['a','e','i','o','u']
v=0
c=0

n=input("enter the string")
n=n.lower()
for i in  n:
  if i in vowels:
    v+=1
  elif i.isalpha():
    c+=1

print("The number of vowels in the string are =",v)
print("The number of consonants in the string are =",c)