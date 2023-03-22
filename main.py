# Imports
import math

# Welcome Code
print("""\n__________        __________        .__                
\______   \___.__.\______   \_______|__| _____   ____  
 |     ___<   |  | |     ___/\_  __ \  |/     \_/ __ \ 
 |    |    \___  | |    |     |  | \/  |  Y Y  \  ___/ 
 |____|    / ____| |____|     |__|  |__|__|_|  /\___  >
           \/                                \/     \/  """)
print("Welcome to PyPrimes!")

# Variables
primes_between = []
prime_numbers = 0

# Functions - Find Prime Numbers
def print_prime():
    try:
        print("")

        start_range = (int(input("Enter the start range: ")))
        end_range = (int(input("Enter the end range: ")))

        print("\nThe following numbers are Prime Numbers: ")

        for num in range(start_range, end_range):
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    print(num)
    except UnboundLocalError:
        print("An unknown error has occured! ERROR CODE: UnboundLocalError")
    except ValueError:
        print("An unknown error has occured! EROOR CODE: ValueError")
    except:
        print("An unknown error has occured!")

# Functions - Check Prime Numbers
def check_prime():
    try:
        print("")
        num_input = int(input("Enter a number to check: "))

        def is_prime(n):
            if n < 2:
                return False

            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return n, "is not a Prime Number."

            return n, "is a Prime Number."

        print(is_prime(num_input))

    except UnboundLocalError:
         print("An unknown error has occured! ERROR CODE: UnboundLocalError")
    except ValueError:
        print("An unknown error has occured! ERROR CODE: ValueError")
    except:
        print("An unknown error has occured!")

# Functions - Find Factors
def find_factors():
    try:
        print("")
        num_input = int(input("Enter number to find its factors: "))
        for i in range(1, num_input + 1):
                if num_input % i == 0:
                    print(i)
    except UnboundLocalError:
        print("An unknown error has occured! ERROR CODE: UnboundLocalError")
    except ValueError:
        print("An unknown error has occured! ERROR CODE: ValueError")
    except:
        print("An unknown error has occured!")

# Main Code
while True:
    print("")
    user_input = str(input("Enter an action: "))

    if user_input == "print.":
        print_prime()
    elif user_input == "check.":
        check_prime()
    elif user_input == "find.":
        find_factors()
    elif user_input == "exit.":
        exit("\nExit requested by user.")
    else:
        print("Invalid Input Detected!")
