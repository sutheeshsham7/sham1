lower = 900
upper = 1000
print("Prime numbers between",lower,"and",upper,"are:")

for h in range(lower,upper + 1):
   if h > 1:
       for i in range(2,h):
           if (h % i) == 0:
               break
       else:
           print(h)
