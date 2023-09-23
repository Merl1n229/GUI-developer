import tkinter as tk
from functools import partial

window = tk.Tk()
window.title('Калькулятор3000')
window.geometry('350x500')
window.resizable(False, False)
window.configure(bg='black')

def calculate(text):
    global formula

    if text == 'C':
        formula = ''
    elif text == 'X^2':
        formula = str((eval(formula)) ** 2)
    elif text == '=' or text == '\r':
        try:
            if ('++' in formula) or ('--' in formula) or ('**' in formula) or ('//' in formula):
                formula = 'Ошибка'
            else:
                formula = str(eval(formula))
        except ZeroDivisionError:
            formula = "На 0 делить\nнельзя!"
        except Exception:
            formula = "Ошибка"
    elif text == 'del' or text == '\x08':
        formula = formula[:-1]
    else:
        if formula == '0':
            formula = ''
        if text in '0123456789/*-+':
            if ((text in '/*-+') and (formula == '' or formula.endswith('+' or '-' or '*' or '/'))):
                formula = formula
            else:
                formula += text
        elif text == '.' and '.' not in formula:  
            formula += text
    label_text.configure(text=formula)


def keypress(event):
    key = event.keysym

    if key == 'Return':
        key = '='
    elif key == 'plus':
        key = '+'
    elif key == 'BackSpace':
        key = 'del'
    elif key == 'minus':
        key = '-'
    elif key == 'asterisk':
        key = '*'  
    elif key == 'slash':
        key = '/'  
    elif key == 'period' or key == 'decimal':  
        key = '.'
    elif key == 'Escape':  
        key = 'C'

    if key:
        calculate(key)



formula = '0'
label_text = tk.Label(text=formula, font=('Roboto', 30, 'bold'), bg='black', fg='white', wraplength=200) # Изменено значение wraplength
label_text.grid(row=0, column=0, columnspan=4, pady=20)

buttons = ['C', 'X^2', '%', '/',
           '7', '8', '9', '*',
           '4', '5', '6', '-',
           '1', '2', '3', '+',
           '0', '.', '=', 'del']

row_val = 1
col_val = 0
for button in buttons:
    tk.Button(text=button, bg='orange', font=('Roboto', 20), command=partial(calculate, button)).grid(row=row_val, column=col_val, sticky='nsew')
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    window.grid_columnconfigure(i, weight=1)
    window.grid_rowconfigure(i+1, weight=1)

window.bind("<Key>", keypress)

window.mainloop()
