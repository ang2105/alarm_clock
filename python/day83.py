#3


def add(a, b):  
    sum = a + b  
    print(a, "+", b, "=", sum) 
def subtract(a, b):  
    difference = a - b  
    print(a, "-", b, "=", difference)  
  
def multiply(a, b):  
    product = a * b  
    print(a, "x", b, "=", product)  
  
def divide(a, b):  
    division = a / b  
    print(a, "/", b, "=", division)  
  
while True:  
    print("MENU")  
    print("1. Addition of two Numbers")  
    print("2. Difference between two Numbers")  
    print("3. Multiplication of two Numbers")  
    print("4. Division of two Numbers")  
    print("5. exit")
    choice = int(input("\nEnter your Choice: "))  
  
    if choice == 1:  
        print( "\nPERFORMING ADDITION\n")  
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        add(a, b)  
  
    elif choice == 2:  
        print( "\nPERFORMING SUBTRACTION\n")  
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        subtract(a, b)  

    elif choice == 3:  
        print( "\nPERFORMING MULTIPLICATION\n")  
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        multiply(a, b)  

    elif choice == 4:  
        print( "\nPERFORMING DIVISION\n")  
        a = int( input("Enter First Number: "))  
        b = int( input("Enter Second Number: "))  
        divide(a, b)  

    elif choice == 5:  
        break
      
    else:  
        print( "Please enter a valid Input from the list") 
