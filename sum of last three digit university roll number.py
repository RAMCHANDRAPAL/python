R=int(input("enter the university roll number"))
a=R%10
R/=10
b=R%10
R/=10
c=R%10
s=int(a)+int(b)+int(c)
print("sum of three last digit=",s)
