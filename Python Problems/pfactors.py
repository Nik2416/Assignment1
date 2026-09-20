n=18
res=[]
for i in range(1,n//2):
  if(n%i==0):
    res.append(i)
res.append(n)
print(res)
