from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("XO Game")
root.geometry("600x600")
root.config(bg="#523b87")

# Reset button
reset_button = Button(root, text="Reset", bg="#8c70cc", fg="white", font=('Arial', 16, 'bold'), padx=20, pady=10,
                      command=lambda: reset_btn())
reset_button.pack()

# Row 1
button11 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button11))
button11.place(x=80, y=100)

button12 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button12))
button12.place(x=230, y=100)

button13 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button13))
button13.place(x=380, y=100)

# Row 2
button21 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button21))
button21.place(x=80, y=250)

button22 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button22))
button22.place(x=230, y=250)

button23 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button23))
button23.place(x=380, y=250)

# Row 3
button31 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button31))
button31.place(x=80, y=400)

button32 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button32))
button32.place(x=230, y=400)

button33 = Button(root, text="", bg="white", font=('Arial', 16, 'bold'), width=10, height=5,
                  command=lambda: on_button_click(button33))
button33.place(x=380, y=400)

player = 'X'


def check_winner():
    # PLayer X
    # Row 1
    if button11['text'] == button12['text'] == button13['text'] == "X":
        button11['bg'] = button12['bg'] = button13['bg'] = "green"
        messagebox.showinfo("Winner", "Player X is the winner")

    # Row 2
    elif button21['text'] == button22['text'] == button23['text'] == "X":
        messagebox.showinfo("Winner", "Player X is the winner")
    # Row 3
    elif button31['text'] == button32['text'] == button33['text'] == "X":
        messagebox.showinfo("Winner", "Player X is the winner")
    # Column 1
    elif button11['text'] == button21['text'] == button31['text'] == "X":
        messagebox.showinfo("Winner", "Player X is the winner")
    # Column 2
    elif button12['text'] == button22['text'] == button32['text'] == "X":
        messagebox.showinfo("Winner", "Player X is the winner")
    # Column 3
    elif button13['text'] == button23['text'] == button33['text'] == "X":
        messagebox.showinfo("Winner", "Player X is the winner")
    # Diagonal
    elif button11['text'] == button22['text'] == button33['text'] == "X":
        messagebox.showinfo("Winner", "Player X is the winner")
    # Diagonal
    elif button13['text'] == button22['text'] == button31['text'] == "X":
        messagebox.showinfo("Winner", "Player X is the winner")

    # PLayer O
    # Row 1
    if button11['text'] == button12['text'] == button13['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")
    # Row 2
    elif button21['text'] == button22['text'] == button23['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")
    # Row 3
    elif button31['text'] == button32['text'] == button33['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")
    # Column 1
    elif button11['text'] == button21['text'] == button31['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")
    # Column 2
    elif button12['text'] == button22['text'] == button32['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")
    # Column 3
    elif button13['text'] == button23['text'] == button33['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")
    # Diagonal
    elif button11['text'] == button22['text'] == button33['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")
    # Diagonal
    elif button13['text'] == button22['text'] == button31['text'] == "O":
        messagebox.showinfo("Winner", "Player O is the winner")


def reset_btn():
    global player
    button11['text'] = ""
    button12['text'] = ""
    button13['text'] = ""

    button21['text'] = ""
    button22['text'] = ""
    button23['text'] = ""

    button31['text'] = ""
    button32['text'] = ""
    button33['text'] = ""
    player = 'X'

    button11['bg'] = "white"
    button12['bg'] = "white"
    button13['bg'] = "white"

    button21['bg'] = "white"
    button22['bg'] = "white"
    button23['bg'] = "white"

    button31['bg'] = "white"
    button32['bg'] = "white"
    button33['bg'] = "white"


def on_button_click(button):
    global player
    if button['text'] == '':
        button['text'] = player

        if player == 'X':
            player = 'O'
        else:
            player = 'X'

        check_winner()


root.mainloop()