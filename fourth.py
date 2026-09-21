kil=float(input("Give Distance in Kilometer"))
mile=kil*0.621371

print("The distance in MILES",mile,"mile") 
 
if (kil>0):
  print('Positive')
elif (kil==0):
  print("Zero")
else:
  print("Negative")