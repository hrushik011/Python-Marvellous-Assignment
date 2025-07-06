def Stars(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*",end=" ")
        print ()
print("Enter the number")
n = int(input())
output = Stars(n)
print("The result is :",output)
