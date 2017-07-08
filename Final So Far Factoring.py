import math
from decimal import *
from fractions import *
from math import *
from functools import reduce

def readInitialValues(equation):
        xPosition = equation.find("x")
        if xPosition == -1:
            print ("Sorry this is not a Quadratic Equation")
            quit()
        elif equation[0] == "x":
            a = 1
        elif equation[0] == "-" and equation[1] == "x":
            a = -1
        else:
            a = a = int(equation[0: xPosition])
        restofEquation = equation[xPosition + 4 :]
        xPosition2 = restofEquation.find("x")
        if xPosition2 == -1:
            b = 0
            restofEquation2 = restofEquation
            c = int(restofEquation2)
        else:
            if restofEquation[0] == "+" and restofEquation[1] == "x":
                b = 1
            elif restofEquation[0] == "-" and restofEquation[1] == "x":
                b = -1
            else:
                b = int(restofEquation[0:xPosition2])
        if (len(restofEquation[xPosition2:])) ==1 and xPosition2 != -1:
            c = 0
        else:
            restofEquation2 = restofEquation[xPosition2+1:]
            c = int( restofEquation2[0:])
        return a,b,c
    
def factorQuadratic(a,b,c):

    # Determines the discriminant of the program using the formula b² - 4ac
    def discriminant(a, b, c):
        discrim = b**Decimal('2')  - Decimal('4') * a * c
        return discrim

    # Determines the roots of the equation with the formula (-b + determinant) / 2a and (-b - determinant) / 2a
    def solve(a, b, c):
        discrim = discriminant(a, b, c)
        # Discriminant of 0 has 1 real root
        if discrim == 0:
            x = Fraction(-b / (2 * a)).limit_denominator()
            return (1, x)
        # Discriminant greater than 0 has 2 real roots
        elif discrim > 0:
            x1 = (-b + discrim.sqrt()) / (2 * a)
            x2 = (-b - discrim.sqrt()) / (2 * a)
            # Output a fractional answer if the answer is rational
            if factors(a, b, c):
                x1 = Fraction(x1).limit_denominator()
                x2 = Fraction(x2).limit_denominator()
            # Otherwise round an irrational number to the nearest hundredth
            else:
                x1 = round(x1, 2)
                x2 = round(x2, 2)
            return (2, x1, x2)
        # Discriminant less than 0 has no real roots
        if discrim < 0:
            return (0,)

    # If the discriminant is a perfect square then the equation is factorable
    def factors(a, b, c):
        discrim = discriminant(a, b, c)
        if isPerfectSquare(discrim):
            return True
        else:
            return False

    # A number is a perfect square if its the nearest integer to itself is itself
    def isPerfectSquare(n):
        root = n.sqrt()
        if int(root + Decimal('0.5'))**2 == n:
            return True
        else:
            return False

    def main():
        
        print("QUADRATIC EQUATION ROOT CALCULATOR")
        print("\nA quadratic equation has the form:")
        print("ax² + bx + c = 0")
        print("where a, b, and c are constants.")
        # Continue running the program until the user specifies to quit
        continueCalculate = ""
        while continueCalculate != "n":
            

            # User the solve function to determine the factors
            factorList = solve(a, b, c)

            # Build the equation component by component
            print("\nThe equation is ", end="")
            # No coefficient if it is 1
            if a == 1:
                print("x²", end="")
            # Only negative sign as coefficient if it is -1
            elif a == -1:
                print("-x²", end="")
            # Otherwise just print the coefficient
            else:
                print("{}x²".format(a), end="")
            # No coefficient if it is 1
            if b == 1:
                print(" + x", end="")
            # Only negative sign as coefficient if it is -1
            elif b == -1:
                print(" - x", end="")
            # Subtract the positive version of the coefficient instead if the coefficient is negative
            elif b < 0:
                print(" - {}x".format(-b), end="")
            # Add if the above does not apply and the coefficient is not 0
            elif b > 0:
                print(" + {}x".format(b), end="")
            # If the coefficient is 0 the coefficient and the variable will not be printed
            # Subtract the positive version of the constant instead if the constant is negative
            if c < 0:
                print(" - {}".format(-c), end="")
            # Add if the above does not apply and the constant is not 0
            elif c > 0:
                print(" + {}".format(c), end="")
            # If the constant is 0 it will not be printed
            print()

            # If the function returns no roots, there are no real roots and is therefore never factorable
            if factorList[0] == 0:
                print("This equation has no real roots.")
                print("The equation is not factorable.")
            # If the function returns one root, there is one real root and since the discriminant is 0, which is a perfect square, it is always factorable
            elif factorList[0] == 1:
                # Output the single root of the equation
                print("This equation has one real root: x = {}".format(factorList[1]))
                print("This equation is factorable.")
                print("The equation can be factored as: ", end="")
                # Build the factored equation component by component
                # Coefficient of the factored equation, i.e., j in the following equation: j(x - a)²
                coefficient = a
                # Another coefficient of the factored equation, i.e. j in the following equation: (jx - a)²
                coefficient1 = 1
                # Determine the second coefficient by distributing the first coefficient across the factored part only if the root is not an integer
                if int(factorList[1]) != factorList[1]:
                    coefficient1 = factorList[1].denominator
                    coefficient /= coefficient1**2
                # Print nothing if the coefficient is 1, '-' if the coefficient is -1, and the coefficient otherwise
                if coefficient == 1:
                    print("", end="")
                elif coefficient == -1:
                    print("-", end="")
                else:
                    print("{}".format(coefficient).rstrip('0').rstrip('.'), end="")
                print("(", end="")
                # Print the second coefficient if it is not 1
                if coefficient1 != 1:
                    print("{}".format(coefficient1), end="")
                print("x".format(coefficient1), end="")
                # Print the root of the equation multiplied by the second coefficient
                if factorList[1] < 0:
                    print(" + {}".format(-factorList[1] * coefficient1).rstrip('0').rstrip('.'), end="")
                elif factorList[1] > 0:
                    print(" - {}".format(factorList[1] * coefficient1).rstrip('0').rstrip('.'), end="")
                print(")²")
            # If the function returns two roots, there are two real roots
            elif factorList[0] == 2:
                # Output the roots of the equation
                print("This equation has two real roots: x = {} and x = {}".format(factorList[1], factorList[2]))
                # Determine whether the equation can be factored with the factorable function
                factorable = factors(a, b, c)
                # If it can be, output the factored form
                if factorable:
                    print("This equation is factorable.")
                    print("The equation can be factored as: ", end="")
                    # Build the factored equation component by component
                    # Coefficient of the factored equation, i.e., j in the following equation: j(x - a)(x - b)
                    coefficient = a
                    # Another coefficient of the factored equation, i.e. j in the following equation: (jx - a)(x - b)
                    coefficient1 = 1
                    # Another coefficient of the factored equation, i.e. j in the following equation: (x - a)(jx - b)
                    coefficient2 = 1
                    # Determine the second coefficient by distributing the first coefficient across the factored part only if the first root is not an integer
                    if int(factorList[1]) != factorList[1]:
                        coefficient1 = factorList[1].denominator
                        coefficient /= coefficient1
                    # Determine the third coefficient by distributing what remains of the first coefficient across the factored part only if the second root is not an integer
                    if int(factorList[2]) != factorList[2]:
                        coefficient2 = factorList[2].denominator
                        coefficient /= coefficient2
                    # Print nothing if the coefficient is 1, '-' if the coefficient is -1, and the coefficient otherwise
                    if coefficient == 1:
                        print("", end="")
                    elif coefficient == -1:
                        print("-", end="")
                    else:
                        print("{}".format(coefficient).rstrip('0').rstrip('.'), end="")
                    print("(", end="")
                    # Print the second coefficient if it is not 1
                    if coefficient1 != 1:
                        print("{}".format(coefficient1), end="")
                    print("x", end="")
                    # Print the first root of the equation multiplied by the second coefficient
                    if factorList[1] < 0:
                        print(" + {}".format(-factorList[1] * coefficient1).rstrip('0').rstrip('.'), end="")
                    elif factorList[1] > 0:
                        print(" - {}".format(factorList[1] * coefficient1).rstrip('0').rstrip('.'), end="")
                    print(")(", end="")
                    # Print the third coefficient if it is not 1
                    if coefficient2 != 1:
                        print("{}x".format(coefficient2), end="")
                    print("x", end="")
                    # Print the second root of the equation multiplied by the third coefficient
                    if factorList[2] < 0:
                        print(" + {}".format(-factorList[2] * coefficient2).rstrip('0').rstrip('.'), end="")
                    elif factorList[2] > 0:
                        print(" - {}".format(factorList[2] * coefficient2).rstrip('0').rstrip('.'), end="")
                    print(")")
                # Otherwise, only tell the user that the equation is not factorable
                else:
                    print("This equation is not factorable.")
            # Prompt the user on whether they want to continue solving and factoring quadratic equations with valid option checking
            continueCalculate = input("\nDo you still want to continue calculating the roots of quadratic equations? (Y / N) ").lower()
            while continueCalculate != "n" and continueCalculate != "y":
                continueCalculate = input("That's not a valid option. Do you still want to continue calculating the roots of quadratic equations? (Y / N) ").lower()

    main()

testCases = ["x**2+6x+5", "x**2+7x+5", "2x**2+12x+10", "x**2-2x+1", "x**2-5x+6",
             "x**2-x-12", "2x**2-2x-24", "4x**2-9", "12x**2-27", "6x**2+5x+1",
             "-20x**2+22x+12", "4x**2-4x+1","8x**2-8x+2","x**2-3","2x**2-6",
             "2x**2-6x", "x**2+6x"]

for i in range (len(testCases)):
    equation = testCases[i]
    a,b,c = readInitialValues(equation)
    factorQuadratic(a,b,c)
    print(a,b,c)

