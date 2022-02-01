
def leapYear(year):
    """
        - this function determines if a year is a leap year or not.
        - flow logic is based on the following premises:
            - a year is a leap year if evenly divided by four
            - excerp for century ending with 00
            - a century year is a leap year if perfectly divided by 400
    """
    if len(str(year)) != 4:
        print("Invalid Year")

    if year % 4 == 0:

        if str(year).endswith("00"):

            if year % 400 == 0:

                print("True")

            else:

                print("False")
        else:
            print("True")
    else:
        print("False")


year = int(input("Enter year: "))
leapYear(year)