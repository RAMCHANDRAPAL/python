li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print("Negative numbers in",li,"are: ")
negative_num = [num for num in li if num < 0]
  
print(negative_num)
