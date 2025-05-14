def CheckNo(no1):
    if no1 >0 :
        return "Positive"
    elif no1 <0:
        return "Negative"
    else:
        return "Zero"
print("Enter number")
no1 = int(input())
output = CheckNo(no1)
print("The number is :",output)