from tkinter import *
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_letters = random.randint(8,10)
number_numbers = random.randint(2,4)
number_symbols = random.randint(2,4)

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="password-manager-start\password-manager-start\logo.png")
logo = canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 12))
website_label.grid(column=0, row=1)

website_input = Entry(width=35)
website_input.grid(column=1,row=1, columnspan=2)
website_input.focus()

username_label = Label(text="Email/Username:", font=("Arial", 12))
username_label.grid(column=0, row=2)

username_input = Entry(width=35)
username_input.grid(column=1,row=2, columnspan=2)

password_label = Label(text="Password:", font=("Arial", 12))
password_label.grid(column=0, row=3)

password_input = Entry(width=21)
password_input.grid(column=1,row=3)

def choice(option):
    pop.destroy()
    if option == "yes":
        information = f"{website_input.get()}  |  {username_input.get()}  |  {password_input.get()}"
        file = open('./password-manager-start/data.txt', 'a')
        file.write(f"{information}\n")
        file.close()
    else:
        pass

def button_clicked():
    global pop
    pop = Toplevel(window)
    pop.geometry("500x150")
    pop.title("Password Confirmation")
    password_confirmation = Label(pop, text=f"Email: {username_input.get()}\nPassword: {password_input.get()}\nIs this ok?")
    password_confirmation.pack()
    
    password_frame = Frame(pop)
    password_frame.pack()

    yes = Button(password_frame, text="Yes", command=lambda: choice("yes"))
    yes.pack()

    no = Button(password_frame, text="No", command=lambda: choice("no"))
    no.pack()

def generate():
    generate_password = []
    for _ in range(number_letters):
        generate_password.append(random.choice(letters))
    for _ in range(number_numbers):
        generate_password.append(random.choice(numbers))
    for _ in range(number_symbols):
        generate_password.append(random.choice(symbols))
    random.shuffle(generate_password)
    result = ''.join(generate_password)
    password_input.delete(0,END)
    password_input.insert(0,result)

generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=button_clicked)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
