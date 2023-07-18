from tkinter import *
import random
import string
import customtkinter
import pyperclip

letters = string.ascii_lowercase
capital_letters = string.ascii_uppercase
numbers = string.digits
special_char = string.punctuation

letter_i = IntVar
cap_letter_i = IntVar
numbers_i = IntVar
specialchar_i = IntVar


window = customtkinter.CTk()
window.update()

# Password Generator Inputs, Checkbox

def inputs():
    window.title("Password Generator")
    window.geometry("375x495")
# Lowercase CheckBox
    if checkbox_lowercase_value.get() == 1:
        lower_case_entry.grid(row=1, column=2, pady=25, ipadx=10)
        lower_case_entry.focus()
    elif checkbox_lowercase_value.get() == 0:
        lower_case_entry.delete(0, END)
        lower_case_entry.insert(0, 0)
        lower_case_entry.grid_remove()
# Uppercase CheckBox
    if checkbox_uppercase_value.get() == 1:
        upper_case_entry.grid(row=2, column=2, pady=25, ipadx=10)
        upper_case_entry.focus()
    elif checkbox_uppercase_value.get() == 0:
        upper_case_entry.delete(0, END)
        upper_case_entry.insert(0, 0)
        upper_case_entry.grid_remove()
# Numbers CheckBox
    if checkbox_numbers_value.get() == 1:
        numbers_entry.grid(row=3, column=2, pady=25, ipadx=10)
        numbers_entry.focus()
    elif checkbox_numbers_value.get() == 0:
        numbers_entry.delete(0, END)
        numbers_entry.insert(0, 0)
        numbers_entry.grid_remove()
# SpecialChar CheckBox
    if checkbox_specialchar_value.get() == 1:
        specialchar_case_entry.grid(row=4, column=2, pady=25, ipadx=10)
        specialchar_case_entry.focus()
    elif checkbox_specialchar_value.get() == 0:
        specialchar_case_entry.delete(0, END)
        specialchar_case_entry.insert(0, 0)
        specialchar_case_entry.grid_remove()


# Lowercase CheckBox
checkbox_lowercase_value = IntVar()
checkbox1 = customtkinter.CTkCheckBox(window, text="", command=inputs, variable=checkbox_lowercase_value, onvalue=1,
                                      offvalue=0)
# Uppercase CheckBox
checkbox_uppercase_value = IntVar()
checkbox2 = customtkinter.CTkCheckBox(window, text="", command=inputs, variable=checkbox_uppercase_value, onvalue=1,
                                      offvalue=0)
# Numbers CheckBox
checkbox_numbers_value = IntVar()
checkbox3 = customtkinter.CTkCheckBox(window, text="", command=inputs, variable=checkbox_numbers_value, onvalue=1,
                                      offvalue=0)
# SpecialChar CheckBox
checkbox_specialchar_value = IntVar()
checkbox4 = customtkinter.CTkCheckBox(window, text="", command=inputs, variable=checkbox_specialchar_value, onvalue=1,
                                      offvalue=0)

# Lowercase CheckBox
checkbox1.grid(row=1, column=1, pady=25, ipadx=10)
# Uppercase CheckBox
checkbox2.grid(row=2, column=1, pady=25, ipadx=10)
# Numbers CheckBox position
checkbox3.grid(row=3, column=1, pady=25, ipadx=10)
# SpecialChar CheckBox position
checkbox4.grid(row=4, column=1, pady=25, ipadx=10)

# Password Generator Text Label
vault_label = customtkinter.CTkLabel(window, text="Password Generator")
vault_label.configure(anchor=CENTER)
vault_label.grid(column=1, row=0)

# Category Labels
letter_label = customtkinter.CTkLabel(window, text="Lower Case Letters")
letter_label.grid(row=1, column=0, pady=25, ipadx=10)
cap_letter_label = customtkinter.CTkLabel(window, text="Upper Case Letters")
cap_letter_label.grid(row=2, column=0, pady=25, ipadx=10)
number_label = customtkinter.CTkLabel(window, text="Numbers", anchor=E)
number_label.grid(row=3, column=0, pady=25, ipadx=10)
sign_label = customtkinter.CTkLabel(window, text="Special characters")
sign_label.grid(row=4, column=0, pady=25, ipadx=10)


# Category Inputs
lower_case_entry = customtkinter.CTkEntry(window, width=20, placeholder_text="0")
lower_case_entry.insert(0, 0)
upper_case_entry = customtkinter.CTkEntry(window, width=20, placeholder_text="0")
upper_case_entry.insert(0, 0)
numbers_entry = customtkinter.CTkEntry(window, width=20, placeholder_text="0")
numbers_entry.insert(0, 0)
specialchar_case_entry = customtkinter.CTkEntry(window, width=20, placeholder_text="0")
specialchar_case_entry.insert(0, 0)

# Password output Text
password_label = customtkinter.CTkLabel(window, text=NONE, width=80, state="disabled", wraplength=150)
password_label.grid(row=6, column=1)


# Password generator main function
def password_generator():

    letter_i = int(lower_case_entry.get())
    cap_letter_i = int(upper_case_entry.get())
    numbers_i = int(numbers_entry.get())
    specialchar_i = int(specialchar_case_entry.get())

    word = random.choices(letters, k=letter_i)
    word_capital = random.choices(capital_letters, k=cap_letter_i)
    number = random.choices(numbers, k=numbers_i)
    specialchar = random.choices(special_char, k=specialchar_i)

    all = word + word_capital + number + specialchar
    all = random.sample(all, k=len(all))

    passw = []

    for i in all:
        passw.append(i)

    password = str("".join(passw))
    password_label.configure(text=password)
    return password


# Password Copy Button
def copy_password():
    pyperclip.copy(password_label.cget("text"))

copy_password_key_button = customtkinter.CTkButton(window, text="Copy Password", command=copy_password)
copy_password_key_button.grid(row=7, column=1, pady=10)

password_out = password_generator()

# Password Generate Button
generate_button = customtkinter.CTkButton(window, text="Generate Password", command=password_generator)
generate_button.grid(row=5, column=1, pady=10)


inputs()

window.mainloop()
