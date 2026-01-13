a=int(input("Enter the Fist Number:"))
b=int(input("Enter The Seconbd Number:"))
c=int(input("Enter The Third Number:"))
if(a>b):
  if(a>c):
    print("A is max")
  else:
    print("C is max")
elif(c>b):
    print("C is max")
else:
    print("B is max")
