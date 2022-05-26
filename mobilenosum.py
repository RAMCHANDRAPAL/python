n=int(input("enter a number"))
s=0
m=n
while n>0:
  r=n%10
  s=s+r
  n//=10
  print(s)
