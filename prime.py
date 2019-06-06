s = int(input("Enter a number: "))  
  
if s > 1:  
   for i in range(2,s):  
       if (s % i) == 0:  
           print(s,"is not a prime number")  
           break  
   else:  
       print(s,"is a prime number")  
         
else:  
   print(s,"is not a prime number")  

