n=input("Enter the number: ")
n=n.lower()
list=[]
for i in n:
  if i not in list:
    list.append(i)
      
print(list)