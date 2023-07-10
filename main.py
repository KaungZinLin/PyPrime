# This code is written by Kaung Zin Lin (ThatMacCat) in Python.
# This is an open-source project uploaded on GitHub (Link: https://github.com/KaungZinLin/PyPrime)
# As this is an open-source project, anyone can easily fork it and re-created a better version.
# If you found any bugs, fixes and suggestions, you can tell me on the "Issues" tab on GitHub.

# CODE INFO
# Python 3.11
# PyCharm CE
# PyPrime 1.8: The Factors Update (Beta - R2)

# COPYRIGHT 2023 THATMACCAT'S CREATIONS.
# THIS CODE IS CREATED ON 26 JUNE 2023.

# Imports
from tkinter import *
from tkinter import messagebox
import math
import random

# Variables
placeholder = []
random_strings = ["PyPrime - Made by unResolved.", "PyPrime - Inspired by a Grade-6 Maths Book",
                  "PyPrime - Used to Cheat.", "PyPrime - Production Ready.", "PyPrime - Made in Myanmar!"]
title = random.choice(random_strings)


# Functions
def print_non_prime():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())

        non_primes = []
        for num in range(2, 101):
            for i in range(2, num):
                if (num % i) == 0:
                    non_primes.append(num)
                    break
        messagebox.showinfo("Results", "Here are all the non-prime numbers: " + str(non_primes))

    except OverflowError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: OverflowError.")
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: ValueError.")
    except:
        messagebox.showerror("Error!", "An unknown error has occurred!")


def print_prime():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
        primes = []

        if (end > 1000000):
            messagebox.showerror("Error!", "Error: The input mustn't be larger than 1000000!")
        elif (start <= 0):
            messagebox.showerror("Error!", "Error: The input must be greater than 0!")
        else:
            for num in range(start, end + 1):
                if num > 1:
                    for i in range(2, int(math.sqrt(num)) + 1):
                        if num % i == 0:
                            break
                    else:
                        primes.append(str(num))
            messagebox.showinfo("Results", "Here are all the prime numbers:\n" + ", ".join(primes))
    except OverflowError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: OverflowError.")
        start_entry.focus()
        end_entry.focus()
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: ValueError.")
        start_entry.focus()
        end_entry.focus()
    except:
        messagebox.showerror("Error!", "An unknown error has occurred!")
        start_entry.focus()
        end_entry.focus()


def check_prime():
    try:
        n = int(check_entry.get())
        if n < 2:
            messagebox.showinfo("Results", f"{n} is NOT a prime number.")
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    messagebox.showinfo("Results", f"{n} is NOT a prime number.")
                    break
            else:
                messagebox.showinfo("Results", f"{n} is a prime number.")
    except OverflowError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: OverflowError.")
        check_entry.focus()
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occured! ERROR CODE: ValueError.")
        check_entry.focus()
    except:
        messagebox.showerror("Error!", "An unknown error has occured!")
        check_entry.focus()


def find_highest_common_factors():
    try:
        n = int(highest_common_factors_not_really_entry.get())

        if n <= 0:
            messagebox.showerror("Error!", "Error: The input must be greater than 0!")
        elif n >= 1000000000:
            messagebox.showerror("Error!", "Error: The input mustn't be larger than 1000000000!")
        else:
            factors = []
            for i in range(1, n + 1):
                if n % i == 0:
                    factors.append(str(i))
            messagebox.showinfo("Results", f"Here are all the factors of {n}:\n" + ", ".join(factors))
    except ValueError:
        messagebox.showerror("Error!", "Error: The input must be a number (int).")
        highest_common_factors_not_really_entry.focus()
    except OverflowError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: OverflowError.")
        highest_common_factors_not_really_entry.focus()
    except:
        messagebox.showerror("Error!", "An unknown error has occurred!")
        highest_common_factors_not_really_entry.focus()


def find_hcf():
    try:
        num_1 = int(lcf_or_hcf_input_entry_first.get())
        num_2 = int(lcf_or_hcf_input_entry_second.get())

        if (num_1 < num_2):
            small_num = num_1
        else:
            small_num = num_2

        for i in range(1, small_num + 1):
            if (num_1 % i == 0 and num_2 % i == 0):
                hcf = i

        messagebox.showinfo("Results", f"HCF of {num_1} and {num_2}: {hcf}")
    except ValueError:
        messagebox.showerror("Error!", "Error: The input must be a number (int)! ")
        lcf_or_hcf_input_entry_first.focus()
        lcf_or_hcf_input_entry_second.focus()
    except:
        messagebox.showerror("Error!", "LCF input must have at least two numbers!")
        lcf_or_hcf_input_entry_first.focus()
        lcf_or_hcf_input_entry_second.focus()


def find_lcf():
    try:
        num_1 = int(lcf_or_hcf_input_entry_first.get())
        num_2 = int(lcf_or_hcf_input_entry_second.get())

        if num_1 > num_2:
            higher = num_1
        else:
            higher = num_2

        value = higher

        while True:
            if higher % num_1 == 0 and higher % num_2 == 0:
                messagebox.showinfo("Results", f"LCF of {num_1} and {num_2}: {higher}")
                break
            else:
                higher += value
    except ValueError:
        messagebox.showerror("Error!", "Error: The input must be a number (int)!")
        lcf_or_hcf_input_entry_first.focus()
        lcf_or_hcf_input_entry_second.focus()
    except:
        messagebox.showerror("Error!", "LCF input must have at least two numbers!")
        lcf_or_hcf_input_entry_first.focus()
        lcf_or_hcf_input_entry_second.focus()


def about_us():
    messagebox.showinfo("About Us",
                        "PyPrime\n" + "\nAn app to Find Prime Numbers in Python.\n" + "Feature 1: Find Prime Numbers within the given range.\n" + "Feature 2: Find non-prime numbers witin the given range.\n" + "Feature 3: Check if Prime Number or not.\n" + "Feature 4: Find Factors of a Number.\n" + "\nNOTE: \n" + "All the answers are checked by a professional and it is correct.\n" + "\nVersion: PyPrime v1.4 (Stable) for macOS" "\nThis version is ONLY for macOS users!\n" + "\nHUGE THANKS FOR USING THIS APP!!!\n" + "Copyright 2023 ThatMacCat's Creations")


# GUI Setup
window = Tk()
window.title("PyPrime 1.8")
window.resizable(False, False)
window.config(padx=50, pady=50)

# Labels
welcome_label = Label(window, text=title, font=("Areal", 25))
welcome_label.grid(row=0, column=0, columnspan=3, sticky='w')

print_label = Label(window, text="\nPRIME/ NON-PRIME NUMBERS")
print_label.grid(row=2, column=0, columnspan=3, sticky='w')

start_label = Label(window, text="Start range:")
start_label.grid(row=3, column=0, sticky='w')

end_label = Label(window, text="End range:")
end_label.grid(row=4, column=0, sticky='w')

check_label = Label(window, text="\nCHECK IF PRIME OR NOT")
check_label.grid(row=7, column=0, columnspan=3, sticky='w')

check_input_label = Label(window, text="Enter a number to check:")
check_input_label.grid(row=8, column=0, sticky='w')

find_factors_label = Label(window, text="\nFACTORS")
find_factors_label.grid(row=9, column=0, columnspan=3, sticky='w')

highest_common_factors_input_label = Label(window, text="Enter a number to find its Factors: ")
highest_common_factors_input_label.grid(row=10, column=0, sticky='w')

more_factors_label = Label(window, text="\nMORE FACTORS")
more_factors_label.grid(row=11, column=0, sticky='w')

lcf_or_hcf_input_label_first = Label(window, text="Enter a Number to find LCF or HCF: ")
lcf_or_hcf_input_label_first.grid(row=12, column=0, sticky='w')

lcf_or_hcf_input_label_second = Label(window, text="Enter another Number to find LCF or HCF: ")
lcf_or_hcf_input_label_second.grid(row=13, column=0, sticky='w')

lowest_common_factors_input_label = Label(window, text="Enter a number to find its LCF: ")
# lowest_common_factors_input_label.grid(row=11, column=0, sticky='w')

copyright_label = Label(window, text="\nCOPYRIGHT 2023 THATMACCAT'S CREATIONS.")
# copyright_label.grid(row=11, column=0, sticky='w')

distribute_label = Label(window, text="DO NOT DISTRIBUTE!")
# distribute_label.grid(row=12, column=0, sticky='w')

website_label = Label(window, text="\nWebsite: kaungzinlin.github.io/pyprime-website")
# website_label.grid(row=13, column=0, sticky='w')

# Entries
start_entry = Entry(window, width=35)
start_entry.grid(row=3, column=1, sticky='w')
start_entry.focus()

end_entry = Entry(window, width=35)
end_entry.grid(row=4, column=1, sticky='w')

check_entry = Entry(window, width=35)
check_entry.grid(row=8, column=1, sticky='w')

highest_common_factors_not_really_entry = Entry(window, width=35)
highest_common_factors_not_really_entry.grid(row=10, column=1, sticky='w')

lowest_common_factors_entry = Entry(window, width=35)
# lowest_common_factors_entry.grid(row=11, column=1, sticky='w')

lcf_or_hcf_input_entry_first = Entry(window, width=35)
lcf_or_hcf_input_entry_first.grid(row=12, column=1, sticky='w')

lcf_or_hcf_input_entry_second = Entry(window, width=35)
lcf_or_hcf_input_entry_second.grid(row=13, column=1, sticky='w')

# Buttons
print_button = Button(window, text="Print Prime", width=10, command=print_prime)
print_button.grid(row=3, column=2, sticky='w')

print_2_button = Button(window, text="Print non-prime", width=10, command=print_non_prime)
print_2_button.grid(row=4, column=2, sticky='w')

check_button = Button(window, text="Check", width=10, command=check_prime)
check_button.grid(row=8, column=2, sticky='w')

factor_button = Button(window, text="Find", width=10, command=find_highest_common_factors)
factor_button.grid(row=10, column=2, sticky='w')

about_button = Button(window, text="About", width=10, command=about_us)
# about_button.grid(row=0, column=2)

find_hcf_button = Button(window, text="Find HCF", width=10, command=find_hcf)
find_hcf_button.grid(row=12, column=2, sticky='w')

find_lcf_button = Button(window, text="Find LCF", width=10, command=find_lcf)
find_lcf_button.grid(row=13, column=2, sticky='w')

# License
license_label = Label(window, text="License: GNU General Public License v3.0.")
license_label.grid(row=15, column=0, sticky='w')

github_label = Label(window, text="\nGitHub: https://github.com/KaungZinLin/PyPrime")
github_label.grid(row=14, column=0, sticky='w')

# Main Loop
window.mainloop()
