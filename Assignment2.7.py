def Display(n):
    for i in  range(n):
        for j in range(1,n+1,1):
            print(j,end = " ")
        print() # used to print on another second line
    result = i
    return result
print("Enter the number")
n = int(input())
output  = Display(n)
