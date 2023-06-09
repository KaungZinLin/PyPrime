# Imports
from tkinter import *
from tkinter import messagebox
import math

# Variables
placeholder = []

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
        for num in range(start, end+1):
            if num > 1:
                for i in range(2, int(math.sqrt(num))+1):
                    if num % i == 0:
                        break
                else:
                    primes.append(str(num))
        messagebox.showinfo("Results", "Here are all the prime numbers:\n" + ", ".join(primes))
    except OverflowError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: OverflowError.")
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: ValueError.")
    except:
        messagebox.showerror("Error!", "An unknown error has occurred!")

def check_prime():
    try:
        n = int(check_entry.get())
        if n < 2:
            messagebox.showinfo("Results", f"{n} is not a prime number.")
        else:
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    messagebox.showinfo("Results", f"{n} is not a prime number.")
                    break
            else:
                messagebox.showinfo("Results", f"{n} is a prime number.")
    except OverflowError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: OverflowError.")
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occured! ERROR CODE: ValueError.")
    except:
        messagebox.showerror("Error!", "An unknown error has occured!")

def find_highest_common_factors():
    try:
        n = int(highest_common_factors_entry.get())

        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(str(i))
        messagebox.showinfo("Results", f"Here are all the factors of {n}:\n" + ", ".join(factors))
    except OverflowError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: OverflowError.")
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occurred! ERROR CODE: ValueError.")
    except:
        messagebox.showerror("Error!", "An unknown error has occurred!")

def about_us():
    messagebox.showinfo("About Us", "PyPrime\n" + "\nAn app to Find Prime Numbers in Python.\n" + "Feature 1: Find Prime Numbers within the given range.\n" + "Feature 2: Find non-prime numbers witin the given range.\n" + "Feature 3: Check if Prime Number or not.\n" + "Feature 4: Find Factors of a Number.\n" + "\nNOTE: \n" + "All the answers are checked by a professional and it is correct.\n" + "\nVersion: PyPrime v1.4 (Stable) for macOS" "\nThis version is ONLY for macOS users!\n" + "\nHUGE THANKS FOR USING THIS APP!!!\n" + "Copyright 2023 ThatMacCat's Creations")

# GUI Setup
window = Tk()
window.title("PyPrime")
# window.iconbitmap('app_icon.ico')
window.resizable(False, False)
# window.geometry("500x500")
window.config(padx=50, pady=50)

# Labels
welcome_label = Label(text="PyPrime", font=("Aeial", 25))
welcome_label.grid(row=0, column=0, columnspan=3, sticky=W)
# 1
print_label = Label(text="\nPRIME/ NON-PRIME NUMBERS")
print_label.grid(row=2, column=0, columnspan=3, sticky=W)

start_label = Label(text="Start range:")
start_label.grid(row=3, column=0, sticky=W)

end_label = Label(text="End range:")
end_label.grid(row=4, column=0, sticky=W)

check_label = Label(text="\nCHECK IF PRIME OR NOT")
check_label.grid(row=7, column=0, columnspan=3, sticky=W)

check_input_label = Label(text="Enter a number to check:")
check_input_label.grid(row=8, column=0, sticky=W)

find_factors_label = Label(text="\nFACTORS")
find_factors_label.grid(row=9, column=0, columnspan=3, sticky=W)

highest_common_factors_input_label = Label(text="Enter a number to find its Factors: ")
highest_common_factors_input_label.grid(row=10, column=0, sticky=W)

lowest_common_factors_input_label = Label(text="Enter a number to find its LCF: ")
# lowest_common_factors_input_label.grid(row=11, column=0, sticky='w')

copyright_label = Label(text="\nCOPYRIGHT 2023 THATMACCAT'S CREATIONS.")
copyright_label.grid(row=11, column=0, sticky='w')

distribute_label = Label(text="DO NOT DISTRIBUTE!")
distribute_label.grid(row=12, column=0, sticky='w')

website_label = Label(text="\nWebsite: kaungzinlin.github.io/pyprime-website")
website_label.grid(row=13, column=0, sticky='w')

# Entries
start_entry = Entry(width=35)
start_entry.grid(row=3, column=1, sticky=W)
start_entry.focus()

end_entry = Entry(width=35)
end_entry.grid(row=4, column=1, sticky=W)

check_entry = Entry(width=35)
check_entry.grid(row=8, column=1, sticky=W)

highest_common_factors_entry = Entry(width=35)
highest_common_factors_entry.grid(row=10, column=1, sticky=W)

lowest_common_factors_entry = Entry(width=35)
# lowest_common_factors_entry.grid(row=11, column=1, sticky=W)

# Buttons
print_button = Button(text="Print Prime", width=10, command=print_prime)
print_button.grid(row=3, column=2, sticky=W)

print_2_button = Button(text="Print non-prime", width=10, command=print_non_prime)
print_2_button.grid(row=4, column=2, sticky=W)

check_button = Button(text="Check", width=10, command=check_prime)
check_button.grid(row=8, column=2, sticky=W)

factor_button = Button(text="Find", width=10, command=find_highest_common_factors)
factor_button.grid(row=10, column=2, sticky=W)

about_button = Button(text="About", width=10, command=about_us)
# about_button.grid(row=0, column=2)

# Main Loop
window.mainloop()
