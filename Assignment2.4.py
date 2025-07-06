def Factors(n):
    factor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
            
    return factor_list


print("Enter number")
n = int(input())

output = Factors(n)
print("The factors are:",output)



 
    