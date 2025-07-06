import Arithematic
def main(): 
    print("Enter First number")
    no1 = int(input())
    print("Enter Second nummber")
    no2 = int(input())
    ans1 = Arithematic.Add(no1,no2)
    ans2= Arithematic.Sub(no1,no2)
    ans3 = Arithematic.Mult(no1,no2)
    ans4 = Arithematic.Div(no1,no2)

    print("The Add is :",ans1)
    print("The Sub is :",ans2)
    print("The Multi is :",ans3)
    print("The Div is :",ans4)

if __name__ == "__main__":
    main()    

