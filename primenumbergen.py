# Opens file where the prime numbers will be stored
# fwpn = File with prime numbers 
fwpn = open('primes.txt', 'w')

#Inputs data for max numbers and creates empty list
MaxNum = int(input("What is the max number?"))
PrimeNumList = []




#prime number generation function
# ** means square root, python memory functions allow for faster computation with squareroot
for x in range (2, MaxNum + 1):
    isPrime = True
    for y in range (2, int (x ** 0.5)+1):
        if x % y == 0:
            isPrime = False
            break
    if isPrime:
        PrimeNumList.append(x)
        
 #finishes the program.            
for items in PrimeNumList:
    fwpn.writelines(items + '\n')

fwpn.close()    
    
