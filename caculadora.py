import tkinter as tk

def clicar(ch):
    if ch == 'C':
        visor.delete(0, tk.END)
        return
    if ch == '=':
        expr = visor.get()
        try:
           
            resultado = str(eval(expr, {"__builtins__": None}, {}))
            visor.delete(0, tk.END)
            visor.insert(0, resultado)
        except Exception:
            visor.delete(0, tk.END)
            visor.insert(0, "Erro")
        return
   
    visor.insert(tk.END, ch)

def backspace(_=None):
    texto = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, texto[:-1])

def enter_igual(_=None):
    clicar('=')


janela = tk.Tk()
janela.title("Calculadora")

visor = tk.Entry(janela, font=("Arial", 24), justify="right")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=8)


layout = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '(', ')'],
]


for r, linha in enumerate(layout, start=1):
    for c, txt in enumerate(linha):
        tk.Button(
            janela, text=txt, width=5, height=2, font=("Arial", 18),
            command=lambda t=txt: clicar(t)
        ).grid(row=r, column=c, padx=5, pady=5, sticky="nsew")


tk.Button(janela, text='C', width=5, height=2, font=("Arial", 18),
          command=lambda: clicar('C')
          ).grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

tk.Button(janela, text='=', width=5, height=2, font=("Arial", 18),
          command=lambda: clicar('=')
          ).grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")


janela.bind('<Return>', enter_igual)
janela.bind('<KP_Enter>', enter_igual)
janela.bind('<BackSpace>', backspace)

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(6):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()