import random
num = random.randint(1,100)
n = int(input("Guess a number btw 1 and 100: "))
attempt = 1

while True:
     if n<1 or n>100:
         print("Error! Number should be between 1 to 100")
         
     elif n<num:
        print("Too low!\n")
        
     elif n>num:
        print("Too high!\n")
        
     else:
        print("Correct")
        break
     
     n=int(input("Guess again: "))
     attempt+=1
     if attempt>=7:
         break

if attempt>=7:
    print("You have used all your 7 attempts. Better luck next time!")
else:
    print("You got it in",attempt,"attempts!")

        


       

       
    







 