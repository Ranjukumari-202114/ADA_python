def expo(a,n):
    if n == 0:
        return 1

    ans = expo(a,n//2)

    if n % 2 == 0:
        ans = ans*ans
    else:

        ans = a*ans*ans
    return ans

def isPrime(n):
    m = n-1
    for a in range(2,n):
        E = expo(a,m)
        if E % n !=1:
            return False
    return True

num = int(input("enter a number: "))
if isPrime(num):
    print("number is prime")
else:
    print("number is not prime")
  
