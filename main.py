import tkinter as tk

root = tk.Tk()
root.geometry('1600x900')
root.title('Sudoku')

#Skapar frames för båda sidor i programmet (startsidan och spel-sidan)
game_page = tk.Frame(root)
start_page = tk.Frame(root)

# Skapar en funktion för att visa startsidan respektive spel-sidan
def show_start_page():
    game_page.pack_forget()  # Dölj spel-sidan
    start_page.pack(fill='both', expand=True)  # Visa startsidan

def show_game_page():
    start_page.pack_forget()  # Dölj startsidan
    game_page.pack(fill='both', expand=True)  # Visa spel-sidan



#Skapar rubrik för startsidan
Label1 = tk.Label(start_page, text='Välkommen till Sudoku!', font=('Times New Roman', 20), fg='black')
Label1.pack(padx=10, pady=10)

#Skapar en knapp för att starta spelet
start_button = tk.Button(start_page, text='Klicka här för att starta spelet', font=('Times New Roman', 18), command=show_game_page)
start_button.pack(padx=10, pady=10)

#Visar nu startsidan
show_start_page()

Label2 = tk.Label(game_page, text='Lycka till!', font=('Times New Roman', 18), fg='black')
Label2.pack(padx=10, pady=10)


#Skapar ett 9x9-rutnät för sudoku-spelet
sudoku_grid = tk.Frame(game_page, bg='black', bd=2, relief='solid')
for i in range(9):
    sudoku_grid.grid_rowconfigure(i, weight=1)
    sudoku_grid.grid_columnconfigure(i, weight=1)

# Skapar celler i rutnätet

def limit_size(P):
    return len(P) <= 1

vcmd = (root.register(limit_size), '%P') #Behöver kanske ändra detta sen (fattar typ inte)

for i in range(9):
    for j in range(9):
        if (j+1) % 3 == 0:
            bottom = 2
            top = 0
        elif (j+1) % 3 == 1:
            top = 2
            bottom = 0
        else:
            top = 0
            bottom = 0

        if (i+1) % 3 == 0:
            right = 2
            left = 0
        elif (i+1) % 3 == 1:
            left = 2
            right = 0
        else:
            left = 0
            right = 0

        square = tk.Entry(
            sudoku_grid, 
            width=2, 
            font=('Times New Roman', 20), 
            justify='center', 
            bg='#f0f0f0', 
            bd=0,
            relief='solid',
            validate='key',
            validatecommand=vcmd,
            highlightthickness=1,
            highlightbackground="#525370",
            highlightcolor="#FF0000",
            )
        
        square.grid(
            row=j,
            column=i, 
            padx=(left, right), 
            pady=(top, bottom), 
            sticky='nsew')

sudoku_grid.pack(padx=10, pady=10)

# Skapar knapparna på spelsidan för att återgå till startsidan
back_button = tk.Button(game_page, text='Tillbaka till startsidan', font=('Times New Roman', 18), command=show_start_page)
back_button.pack(pady=10)

#give_up_button = tk.Button(game_page, text='Klicka här för att ge upp', font=('Times New Roman', 18), command=solve_puzzle)







'''
for i in range(9):
    for j in range(9):
        cell = tk.Entry(sudoku_grid, width=2, font=('Times New Roman', 20), justify='center')
        cell.grid(row=i, column=j, padx=5, pady=5)
        if (i // 3 + j // 3) % 2 == 0:
            cell.config(bg='#f0f0f0')  # Ljus bakgrund för varannan ruta
        else:
            cell.config(bg='#d0d0d0')  # Mörkare bakgrund för varannan ruta

sudoku_grid.pack(padx=10, pady=10)
'''




if __name__ == "__main__":
    root.mainloop()