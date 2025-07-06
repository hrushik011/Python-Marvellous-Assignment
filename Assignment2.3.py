def Factorial(no):
    result = 1
    for i in range(1,no+1):
        result  *= i
    return result
print("Enter the number")
no = int(input())

output = Factorial(no)
print("The result is",output)
