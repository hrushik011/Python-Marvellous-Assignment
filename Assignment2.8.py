def Display(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end = " " )
        print()
    result = i
    return result
print("Enter the number")
n = int(input())
output = Display(n)
print("The ans is:",output)