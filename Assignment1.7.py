def TF(no1):
    if no1 % 5 == 0:
            return "True"
    else:
          return "False"
print("Enter no")
no1 = int(input())
output = TF(no1)
print("The no is :",output)
