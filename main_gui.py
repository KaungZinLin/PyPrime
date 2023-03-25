# Imports
from tkinter import *
from tkinter import messagebox
import math

# Functions
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
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occured! ERROR CODE: ValueError.")
    except:
        messagebox.showerror("Error!", "An unknown error has occured!")

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
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occured! ERROR CODE: ValueError.")
    except:
        messagebox.showerror("Error!", "An unknown error has occured!")

def find_factors():
    try:
        n = int(factor_entry.get())
        factors = []
        for i in range(1, n+1):
            if n % i == 0:
                factors.append(str(i))
        messagebox.showinfo("Results", f"Here are all the factors of {n}:\n" + ", ".join(factors))
    except ValueError:
        messagebox.showerror("Error!", "An unknown error has occured! ERROR CODE: ValueError.")
    except:
        messagebox.showerror("Error!", "An unknown error has occured!")

# GUI Setup
window = Tk()
window.title("PyPrime - GUI (DEV)")
window.config(padx=50, pady=50)

# Labels
welcome_label = Label(text="Welcome to PyPrime!", font="20")
welcome_label.grid(row=0, column=0, columnspan=3)

print_label = Label(text="Print out prime numbers within the given range:")
print_label.grid(row=1, column=0, sticky=W)

start_label = Label(text="Start range:")
start_label.grid(row=2, column=0, sticky=W)

end_label = Label(text="End range:")
end_label.grid(row=3, column=0, sticky=W)

check_label = Label(text="Check if a number is prime:")
check_label.grid(row=5, column=0, sticky=W)

check_input_label = Label(text="Enter a number to check:")
check_input_label.grid(row=6, column=0, sticky=W)

find_factors_label = Label(text="Find factors of a number:")
find_factors_label.grid(row=8, column=0, sticky=W)

factors_input_label = Label(text="Enter a number to find its factors:")
factors_input_label.grid(row=9, column=0, sticky=W)

# Entries
start_entry = Entry(width=35)
start_entry.grid(row=2, column=1)
start_entry.focus()

end_entry = Entry(width=35)
end_entry.grid(row=3, column=1)

check_entry = Entry(width=35)
check_entry.grid(row=6, column=1)

factor_entry = Entry(width=35)
factor_entry.grid(row=9, column=1)

# Buttons
print_button = Button(text="Print", width=10, command=print_prime)
print_button.grid(row=3, column=2)

check_button = Button(text="Check", width=10, command=check_prime)
check_button.grid(row=6, column=2)

factor_button = Button(text="Find", width=10, command=find_factors)
factor_button.grid(row=9, column=2)

# Main Loop
window.mainloop()
