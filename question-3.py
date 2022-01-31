
def drawTriangle(sides):
    """
        - this function draws an inverted triangle
        - increases the actual size by 100%
        - computes the the triangle by decreasing the sides while increasing white space
        - to ensure that a perfect triangle is formed, 1 is added for sides of even number

    """
    numberOfWhiteSpace = 1

    sides = sides * 2

    if sides % 2 == 0:
        sides = sides + 1

    for side in range(sides):

        esterics = '*' * int(sides - side)

        blank = " " * side

        print(f"{blank}{esterics}{blank}")

        numberOfWhiteSpace += 1

        sides -= 1

drawTriangle(30)