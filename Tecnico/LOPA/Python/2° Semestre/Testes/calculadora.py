import tkinter as tk

def pressionar_botao(num):
    expressao_atual = tela.get()
    tela.delete(0, tk.END)
    tela.insert(tk.END, expressao_atual + str(num))

def limpar_tela():
    tela.delete(0, tk.END)

def calcular():
    try:
        expressao = tela.get()
        if "/0" in expressao:
            resultado = "Erro: Div Zero"
        else:
            resultado = eval(expressao)
        
        tela.delete(0, tk.END)
        tela.insert(tk.END, str(resultado))
    except Exception:
        tela.delete(0, tk.END)
        tela.insert(tk.END, "Erro")

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.configure(bg="#202020")
tela = tk.Entry(janela, font=("Arial", 24), bg="#202020", fg="#ffffff", borderwidth=0, justify="right")
tela.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

estilo_botoes = {"font": ("Arial", 14), "bg": "#333333", "fg": "#ffffff", "borderwidth": 0, "activebackground": "#444444"}
estilo_operadores = {"font": ("Arial", 14), "bg": "#f39c12", "fg": "#ffffff", "borderwidth": 0, "activebackground": "#e67e22"}

botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (texto, linha, coluna) in botoes:
    estilo = estilo_operadores if texto in ['/', '*', '-', '+', '='] else estilo_botoes
    
    if texto == '=':
        comando = calcular
    elif texto == 'C':
        comando = limpar_tela
    else:
        comando = lambda t=texto: pressionar_botao(t)
        
    btn = tk.Button(janela, text=texto, command=comando, **estilo)
    btn.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

for i in range(5):
    janela.rowconfigure(i, weight=1)
for j in range(4):
    janela.columnconfigure(j, weight=1)

janela.mainloop()
