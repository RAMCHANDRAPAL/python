s = 0
number = int(input("Enter number: "))
temp = number
while(number):
   i = 1
   facto = 1
   remainder = number % 10
   while(i <= remainder):
      facto = facto * i
      i = i + 1
   s = s + facto
   number = number // 10

if(s == temp):
   print("Strong number")
else:
   print("not a strong number")
