def swap(x,y): 
    print(“Before swapping a :”,x)
    print(“Before swapping b :”,y)
    x,y=y,x
    print(“After swapping a becomes :”,x)
    print(“After swapping b becomes :”,y)

a=int(input(“Enter value : “))
b=int(input(“Enter value : “))  

swap(a,b)  
