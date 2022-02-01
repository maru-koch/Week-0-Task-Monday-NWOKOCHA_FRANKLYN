
def factorialCalcualtor(number):
    """
        ASSIGNMENT - Question 1

        - This function calculates the factorial of an integer using\
          the formula n! = n(n-1)!

    """
    factorial = number
    
    for index in range(1, number):
        
        factorial *= number - index

    # - you may comment out the PRINT STATEMENT

    print(f"The factorial of {number} is {factorial}")

    return f"The factorial for {number} is {factorial}"
    

number = int(input("Enter an Integer: "))

factorialCalcualtor(number)