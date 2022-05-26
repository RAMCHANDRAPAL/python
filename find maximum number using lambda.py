x=int(input("enter a number:"))
y=int(input("enter a number:"))
maximum= lambda a,b:a if a>b else b
print(f"{maximum(x,y)} is a maximum number")
