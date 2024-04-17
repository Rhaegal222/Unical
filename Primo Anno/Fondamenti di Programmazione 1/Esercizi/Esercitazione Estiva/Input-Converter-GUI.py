import tkinter as tk
from tkinter.constants import END

root = tk.Tk()

name_var = tk.StringVar()

def main():
    inserito = name_var.get()
    convertito = conversione(inserito)
    textwidget = tk.Text()
    textwidget.insert(tk.END, convertito)
    textwidget.grid(row=4, column=0, sticky='WE', pady=20, padx=20)

def conversione(inserito):
    lista = []
    stringa = ''
    for i in inserito:
        if i == ' ':
            i = '\n'
            stringa += i
        else:
            stringa += i
    return stringa
    
input_label = tk.Label(root, text = "Inserisci l'input da convertire", font=('calibre',10, 'bold'))
input_label.grid(row=1, column=0, sticky='WE', pady=5, padx=5)

input_entry = tk.Entry(root, textvariable = name_var, font=('calibre',10,'normal'))
input_entry.grid(row=2, column=0, sticky='WE', pady=20, padx=20)

start_button = tk.Button(root, text='Converti', command = main)
start_button.grid(row=3, column=0, sticky='WE', pady=20, padx=20)

root.geometry('400x700')
root.title('Input Converter 2021')
root.configure(background='grey')
root.grid_columnconfigure(0, weight=1)

root.mainloop()