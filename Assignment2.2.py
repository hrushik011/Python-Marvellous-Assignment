def Stars(n):
    for i in range(1,n+1):
        print("* " * (n+1))
        result = i
    return result
print("Enter the number")
n = int(input())
output = Stars(n)
print("The result is :",output)
