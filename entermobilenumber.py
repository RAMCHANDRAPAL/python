n=int(input("Enter your mobile number:"))
s1=s2=x=0
while n>o:
  r=n%10
  if x%2==0:
    s1+=r
    else:
      s2+=r
    x+=1
    n=n//10
    if s1=s2:
      print("Magic number")
      else:
        print("Not magic number")
      
