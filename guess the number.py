    n1 = int(input("Enter the smallest number in the given range :"))
# It returns the smallest number in the given range

n2 = int(input("Enter the biggest number in the given range :"))
# It returns the biggest number in the given range

n3 = int((n1 + n2) / 2)
# It returns the average of the n1 and n2

n = int(input("Enter the number to be guessed : "))
# It returns the value that should be guessed

c = 0 
# to find the  no.of guesses occured we took  a variable c and assigned to 0

while True :
    g = int(input("Guess the number :"))

    if n < g :
        print("Try again! , You guessed too high")
        c+=1
    elif n > g :
        print("Try again!, You guessed too small")
        c+=1
    else :
        print("You guessed the number")
        c+=1
        break
    
 
print("no . of guesses :",c)
 
    

    
