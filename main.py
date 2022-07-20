''' RSA ALGORITHM. BY: ANDREW KARIUKI.'''

import math

# RSA Program
class RSAProgram():
    def __init__(self):
        print("RSA PROGRAM")
        print("*****************************************************\n\n\n")
        self.primes = [2, 3]
        self.candidate = 5

    # Check if Input's are Prime
    '''CHECK IF A NUMBER IS PRIME.'''
    def prime_check(n):
        if(n==2):
            return True
        elif((n<2) or ((n%2)==0)):
            return False
        elif(n>2):
            for i in range(2,n):
                if not(n%i):
                    return False
        return True
    
    check_p = prime_check(p)
    check_q = prime_check(q)
    while(((check_p==False)or(check_q==False))):
        p = int(input("Enter a prime number for p: "))
        q = int(input("Enter a prime number for q: "))
        check_p = prime_check(p)
        check_q = prime_check(q)
        
    # RSA Modulus
    '''COMPUTE THE VALUE FOR n=p*q'''
    n = p * q
    print("RSA Modulus(n) is:", n)
    print("*****************************************************\n\n\n")
    
    #Eulers Toitent
    '''Determining the Totient = (p-1) (q-1)'''
    r= (p-1)*(q-1)
    print("Eulers Toitent(r) is:",r)
    print("*****************************************************\n\n\n")
    
if __name__ == "__main__":
    RSAProgram()