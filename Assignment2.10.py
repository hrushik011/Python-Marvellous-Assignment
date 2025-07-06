def Bot(n):
    Add = 0 
    for i in range(len(n)):
        Add = Add + int(n[i]) # used to convert str to int 
        # no need of print(i) cause it prints iterations
        
        
    return Add

print("Enter the number")
n = input() # cause here we took input as string to be compatibnle with len
output = Bot(n)
print("The addition is :",output)

