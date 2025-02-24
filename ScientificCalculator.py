import math

class ScientificCalculator:
    @staticmethod
    def square_root(x):
        if x < 0:
            raise ValueError("Square root of negative number is not allowed")
        return math.sqrt(x)

    @staticmethod
    def factorial(x):
        if x < 0:
            raise ValueError("Factorial of negative number is not defined")
        return math.factorial(x)

    @staticmethod
    def natural_log(x):
        if x <= 0:
            raise ValueError("Natural logarithm undefined for non-positive values")
        return math.log(x)

    @staticmethod
    def power(base, exponent):
        return math.pow(base, exponent)


def display_menu():
    print("\n🔢Calculator Menu")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice : ")
        try:
            if choice == '1':
                num = float(input("Enter a number: "))
                print(f"√{num} = {ScientificCalculator.square_root(num)}")

            elif choice == '2':
                num = int(input("Enter a non-negative integer: "))
                print(f"{num}! = {ScientificCalculator.factorial(num)}")

            elif choice == '3':
                num = float(input("Enter a positive number: "))
                print(f"ln({num}) = {ScientificCalculator.natural_log(num)}")

            elif choice == '4':
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                print(f"{base}^{exponent} = {ScientificCalculator.power(base, exponent)}")

            elif choice == '5':
                print("Exiting Calculator")
                break
            else:
                print("Invalid choice! Please enter a valid choice")

        except ValueError as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()