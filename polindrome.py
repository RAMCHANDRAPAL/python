n=int(input("enter a number"))
s=0
m=n
while n>0:
  r=n%10
  s=s*10+r
  n//=10
  if s==m:
    print("polindrome")
    else:
    print("not polindrome")
