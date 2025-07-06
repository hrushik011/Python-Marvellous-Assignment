def ChkPrime(no):
    if no<= 1:
        return False
    elif no >1:
        for i in range (2,no):
            if no % i == 0:
                return False
        return True

print("Enter the number")
n = int(input())
if ChkPrime(n):
    print("Prime")
else:
    print("Not Prime")
    






