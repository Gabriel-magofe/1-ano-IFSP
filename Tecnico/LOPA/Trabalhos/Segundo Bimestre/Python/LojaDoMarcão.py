import tkinter as ap
from tkinter import ttk
from tkinter import messagebox


class Produto():
    def __init__(self, produto, preço):
        self.produdo = produto
        self.custo = preço
        self.quantidade = 0
        self.estoque = 100
        

    def total(self):
        return self.custo * self.quantidade
    

class Usuario():
    def __init__(self, senha, pessoa):
        self.cara = pessoa
        self.senha = senha
        self.compras = 0
        self.ultimo1 = None
        self.ultimo2 = None
        self.ultimo3 = None

usuarios = {}

motor = Produto("Motor V8", 1900.90)

supercharger = Produto("supercharger", 1300.00)

bom_d_agua = Produto("Bomba d'água", 300.00)

bom_oleo = Produto("Bomba de olho", 82.29)



TELA = ap.Tk()
TELA.title("Loja Do Marcão")
# TELA.geometry("1920x1080")
TELA.configure(background="#5F5F5F")

estilo = ttk.Style()
estilo.theme_use("alt")

abas = ttk.Notebook(TELA)
abas.pack(expand=True, fill="both")

aba1 = ttk.Frame(abas)
abas.add(aba1, text="Login")

aba2 = ttk.Frame(abas)
abas.add(aba2, text="Compra")

'''aba2_2 = ttk.Frame(abas)
abas.add(aba2_2, text="Compra")'''

aba3 = ttk.Frame(abas)
abas.add(aba3, text="Pagamento")


estilo.configure("Cinza.TFrame", background="#5F5F5F")
aba1.configure(style="Cinza.TFrame")
aba2.configure(style="Cinza.TFrame")
#aba2_2.configure(style="Cinza.TFrame")
aba3.configure(style="Cinza.TFrame")

texto = ap.Label(aba2, text="Faça Login Primeiro",  background="#5F5F5F", fg="#FF8800")
texto.grid(row=1,column=2, columnspan=2,padx=10,pady=10)

'''texto2 = ap.Label(aba2_2, text="Faça Login Primeiro",  background="#5F5F5F", fg="#FF8800")
texto2.grid(row=1,column=2,padx=10,pady=10)'''

texto2 = ap.Label(aba3, text="Faça Login Primeiro", font=("SegoeUI", 9), background="#5F5F5F", fg="#FF8800")
texto2.grid(row=1,column=2,padx=10,pady=10)



img_motor = ap.PhotoImage(file="motor.png")
motor_selc = ap.Label(aba2, text=f"Selecionados: {motor.quantidade}", background="#5F5F5F", fg="#FF8800")

img_charge = ap.PhotoImage(file="Supercharger.png")
charge_selc = ap.Label(aba2, text=f"Selecionados: {supercharger.quantidade}", background="#5F5F5F", fg="#FF8800")

img_bom_d_agua = ap.PhotoImage(file="bomba d_agua.png")
bomb_d_agua_selc = ap.Label(aba2, text=f"Selecionados: {bom_d_agua.quantidade}", background="#5F5F5F", fg="#FF8800")

img_bom_oleo = ap.PhotoImage(file="bomba de óleo.png")
bomb_oleo_selc = ap.Label(aba2, text=f"Selecionados: {bom_oleo.quantidade}", background="#5F5F5F", fg="#FF8800")


compras = {}


pagamentos = {}



def add_motor():
    if motor.quantidade < motor.estoque:
        motor.quantidade += 1
        motor_selc.config(text=f"Selecionados: {motor.quantidade}")
def sub_motor():
    if motor.quantidade > 0:
        motor.quantidade -= 1
        motor_selc.config(text=f"Selecionados: {motor.quantidade}")

def add_supercharger():
    if supercharger.quantidade < supercharger.estoque:
        supercharger.quantidade += 1
        charge_selc.config(text=f"Selecionados: {supercharger.quantidade}")
def sub_supercharger():
    if supercharger.quantidade > 0:
        supercharger.quantidade -= 1
        charge_selc.config(text=f"Selecionados: {supercharger.quantidade}")

def add_bom_d_agua():
    if bom_d_agua.quantidade < bom_d_agua.estoque:
        bom_d_agua.quantidade += 1
        bomb_d_agua_selc.config(text=f"Selecionados: {bom_d_agua.quantidade}")
def sub_bom_d_agua():
    if bom_d_agua.quantidade > 0:
        bom_d_agua.quantidade -= 1
        bomb_d_agua_selc.config(text=f"Selecionados: {bom_d_agua.quantidade}")

def add_bom_oleo():
    if bom_oleo.quantidade < bom_oleo.estoque:
        bom_oleo.quantidade += 1
        bomb_oleo_selc.config(text=f"Selecionados: {bom_oleo.quantidade}")
def sub_bom_oleo():
    if bom_oleo.quantidade > 0:
        bom_oleo.quantidade -= 1
        bomb_oleo_selc.config(text=f"Selecionados: {bom_oleo.quantidade}")

def pago1():
    global total_p

    usuarios[entrada1.get()].compras += 1
    usuarios[entrada1.get()].ultimo3 = usuarios[entrada1.get()].ultimo2
    usuarios[entrada1.get()].ultimo2 = usuarios[entrada1.get()].ultimo1
    usuarios[entrada1.get()].ultimo1 = total_p

    motor.estoque -= motor.quantidade
    motor.quantidade = 0
    supercharger.estoque -= supercharger.quantidade
    supercharger.quantidade = 0
    bom_d_agua.estoque -= bom_d_agua.quantidade
    bom_d_agua.quantidade = 0
    bom_oleo.estoque -= bom_oleo.quantidade
    bom_oleo.quantidade = 0
    
    produto.config(text=f"{motor.produdo} com {motor.estoque} no estoque")
    produto2.config(text=f"{supercharger.produdo} com {supercharger.estoque} no estoque")
    produto3.config(text=f"{bom_d_agua.produdo} com {bom_d_agua.estoque} no estoque")
    produto4.config(text=f"{bom_oleo.produdo} com {bom_oleo.estoque} no estoque")

    motor_selc.config(text=f"Selecionados: {motor.quantidade}")
    charge_selc.config(text=f"Selecionados: {supercharger.quantidade}")
    bomb_d_agua_selc.config(text=f"Selecionados: {bom_d_agua.quantidade}")
    bomb_oleo_selc.config(text=f"Selecionados: {bom_oleo.quantidade}")

    texto2.config(text="Aperte o botão para ver o total")
    if "b_2" in pagamentos: 
        pagamentos["b_2"].grid_forget()
    if "b_3" in pagamentos: 
        pagamentos["b_3"].grid_forget()
    if "b_4" in pagamentos: 
        pagamentos["b_4"].grid_forget()
    if "c" in pagamentos: 
        pagamentos["c"].grid_forget()
    if "p_1" in pagamentos: 
        pagamentos["p_1"].grid_forget()
    if "p_2" in pagamentos: 
        pagamentos["p_2"].grid_forget()
    if "p_3" in pagamentos:
        pagamentos["p_3"].grid_forget()
    if "t_1" in pagamentos: 
        pagamentos["t_1"].grid_forget()
    if "t_2" in pagamentos: 
        pagamentos["t_2"].grid_forget()
    if "t_3" in pagamentos: 
        pagamentos["t_3"].grid_forget()
    if "t_4" in pagamentos: 
        pagamentos["t_4"].grid_forget()



def pago2():
    global total_v

    usuarios[entrada1.get()].compras += 1
    usuarios[entrada1.get()].ultimo3 = usuarios[entrada1.get()].ultimo2
    usuarios[entrada1.get()].ultimo2 = usuarios[entrada1.get()].ultimo1
    usuarios[entrada1.get()].ultimo1 = total_v

    motor.estoque -= motor.quantidade
    motor.quantidade = 0
    supercharger.estoque -= supercharger.quantidade
    supercharger.quantidade = 0
    bom_d_agua.estoque -= bom_d_agua.quantidade
    bom_d_agua.quantidade = 0
    bom_oleo.estoque -= bom_oleo.quantidade
    bom_oleo.quantidade = 0
    
    produto.config(text=f"{motor.produdo} com {motor.estoque} no estoque")
    produto2.config(text=f"{supercharger.produdo} com {supercharger.estoque} no estoque")
    produto3.config(text=f"{bom_d_agua.produdo} com {bom_d_agua.estoque} no estoque")
    produto4.config(text=f"{bom_oleo.produdo} com {bom_oleo.estoque} no estoque")

    motor_selc.config(text=f"Selecionados: {motor.quantidade}")
    charge_selc.config(text=f"Selecionados: {supercharger.quantidade}")
    bomb_d_agua_selc.config(text=f"Selecionados: {bom_d_agua.quantidade}")
    bomb_oleo_selc.config(text=f"Selecionados: {bom_oleo.quantidade}")

    texto2.config(text="Aperte o botão para ver o total")
    if "b_2" in pagamentos: 
        pagamentos["b_2"].grid_forget()
    if "b_3" in pagamentos: 
        pagamentos["b_3"].grid_forget()
    if "b_4" in pagamentos: 
        pagamentos["b_4"].grid_forget()
    if "c" in pagamentos: 
        pagamentos["c"].grid_forget()
    if "p_1" in pagamentos: 
        pagamentos["p_1"].grid_forget()
    if "p_2" in pagamentos: 
        pagamentos["p_2"].grid_forget()
    if "p_3" in pagamentos:
        pagamentos["p_3"].grid_forget()
    if "t_1" in pagamentos: 
        pagamentos["t_1"].grid_forget()
    if "t_2" in pagamentos: 
        pagamentos["t_2"].grid_forget()
    if "t_3" in pagamentos: 
        pagamentos["t_3"].grid_forget()
    if "t_4" in pagamentos: 
        pagamentos["t_4"].grid_forget()


def pago3():

    usuarios[entrada1.get()].compras += 1
    usuarios[entrada1.get()].ultimo3 = usuarios[entrada1.get()].ultimo2
    usuarios[entrada1.get()].ultimo2 = usuarios[entrada1.get()].ultimo1
    usuarios[entrada1.get()].ultimo1 = "Um rim"

    motor.estoque -= motor.quantidade
    motor.quantidade = 0
    supercharger.estoque -= supercharger.quantidade
    supercharger.quantidade = 0
    bom_d_agua.estoque -= bom_d_agua.quantidade
    bom_d_agua.quantidade = 0
    bom_oleo.estoque -= bom_oleo.quantidade
    bom_oleo.quantidade = 0
    
    produto.config(text=f"{motor.produdo} com {motor.estoque} no estoque")
    produto2.config(text=f"{supercharger.produdo} com {supercharger.estoque} no estoque")
    produto3.config(text=f"{bom_d_agua.produdo} com {bom_d_agua.estoque} no estoque")
    produto4.config(text=f"{bom_oleo.produdo} com {bom_oleo.estoque} no estoque")

    motor_selc.config(text=f"Selecionados: {motor.quantidade}")
    charge_selc.config(text=f"Selecionados: {supercharger.quantidade}")
    bomb_d_agua_selc.config(text=f"Selecionados: {bom_d_agua.quantidade}")
    bomb_oleo_selc.config(text=f"Selecionados: {bom_oleo.quantidade}")

    texto2.config(text="Aperte o botão para ver o total")
    if "b_2" in pagamentos: 
        pagamentos["b_2"].grid_forget()
    if "b_3" in pagamentos: 
        pagamentos["b_3"].grid_forget()
    if "b_4" in pagamentos: 
        pagamentos["b_4"].grid_forget()
    if "c" in pagamentos: 
        pagamentos["c"].grid_forget()
    if "p_1" in pagamentos: 
        pagamentos["p_1"].grid_forget()
    if "p_2" in pagamentos: 
        pagamentos["p_2"].grid_forget()
    if "p_3" in pagamentos:
        pagamentos["p_3"].grid_forget()
    if "t_1" in pagamentos: 
        pagamentos["t_1"].grid_forget()
    if "t_2" in pagamentos: 
        pagamentos["t_2"].grid_forget()
    if "t_3" in pagamentos: 
        pagamentos["t_3"].grid_forget()
    if "t_4" in pagamentos: 
        pagamentos["t_4"].grid_forget()





total = None
total_p = None
total_v = None

produto = ap.Label(aba2, text=f"{motor.produdo} com {motor.estoque} no estoque", background="#5F5F5F", fg="#FF8800")
produto2 = ap.Label(aba2, text=f"{supercharger.produdo} com {supercharger.estoque} no estoque", background="#5F5F5F", fg="#FF8800")
produto3 = ap.Label(aba2, text=f"{bom_d_agua.produdo} com {bom_d_agua.estoque} no estoque", background="#5F5F5F", fg="#FF8800")
produto4 = ap.Label(aba2, text=f"{bom_oleo.produdo} com {bom_oleo.estoque} no estoque", background="#5F5F5F", fg="#FF8800")


def show_total():
    global total_p, total_v, total
    total = motor.total() + supercharger.total() + bom_d_agua.total() + bom_oleo.total()
    total_p = round(total + 0.2*total, 2)
    total_v = round(total - 0.1*total, 2)
    texto2.config(text=f"{usuarios[entrada1.get()].cara} sua compra deu R${total}", font=("SegoeUI", 13))

    pagamentos["t_1"] = ap.Label(aba3, text=f"Pagando parcelado em 12X: R${total_p}", background="#5F5F5F", fg="#FFC400")
    pagamentos["t_1"].grid(row=3, column=1, padx=10, pady=10)
    pagamentos["b_2"] = ap.Button(aba3, text="Pagar parcelado", command=pago1, bg="#1290f7", fg="#1fe08f")
    pagamentos["b_2"].grid(row=4, column=1, padx=10, pady=10)

    pagamentos["t_2"] = ap.Label(aba3, text=f"Pagando a vista: R${total_v}", background="#5F5F5F", fg="#FFC400")
    pagamentos["t_2"].grid(row=3, column=2, padx=10, pady=10)
    pagamentos["b_3"] = ap.Button(aba3, text="Pagar a Vista", command=pago2, bg="#1290f7", fg="#1fe08f")
    pagamentos["b_3"].grid(row=4, column=2, padx=10, pady=10)

    if total >= 10000:
        pagamentos["t_3"] = ap.Label(aba3, text=f"Pagar com seu rim", background="#5F5F5F", fg="#FFC400")
        pagamentos["t_3"].grid(row=3, column=3, padx=10, pady=10)
        pagamentos["b_4"] = ap.Button(aba3, text="Pagar com rim", command=pago3, bg="#1290f7", fg="#1fe08f")
        pagamentos["b_4"].grid(row=4, column=3, padx=10, pady=10)

    pagamentos["c"] = ap.Label(aba3, text=f"{usuarios[entrada1.get()].compras} compras realizadas conosco", background="#5F5F5F", fg="#FF8800")
    pagamentos["c"].grid(row=2, column=4, padx=80, pady=10)
    pagamentos["t_4"] = ap.Label(aba3, text="Ultimas compras:", background="#5F5F5F", fg="#FF8800")
    pagamentos["t_4"].grid(row=3, column=4, padx=80, pady=10)
    pagamentos["p_1"] = ap.Label(aba3, text=f"Ultima compra paga com: {usuarios[entrada1.get()].ultimo1}", background="#5F5F5F", fg="#FF8800")
    pagamentos["p_1"].grid(row=4, column=4, padx=80, pady=10)
    pagamentos["p_2"] = ap.Label(aba3, text=f"Penúltima compra paga com: {usuarios[entrada1.get()].ultimo2}", background="#5F5F5F", fg="#FF8800")
    pagamentos["p_2"].grid(row=5, column=4, padx=80, pady=10)
    pagamentos["p_3"] = ap.Label(aba3, text=f"Atepenúltima compra paga com: {usuarios[entrada1.get()].ultimo3}", background="#5F5F5F", fg="#FF8800")
    pagamentos["p_3"].grid(row=6, column=4, padx=80, pady=10)

def logaut():
    texto.config( text="Faça Login Primeiro",  background="#5F5F5F", fg="#FF8800")
    texto2.config( text="Faça Login Primeiro",  background="#5F5F5F", fg="#FF8800")

    produto.grid_forget()
    produto2.grid_forget()
    produto3.grid_forget()
    produto4.grid_forget()

    charge_selc.grid_forget()
    motor_selc.grid_forget()
    bomb_d_agua_selc.grid_forget()
    bomb_oleo_selc.grid_forget()

    compras["b_1"].grid_forget()
    compras["b_2"].grid_forget()
    compras["b_3"].grid_forget()
    compras["b_4"].grid_forget()
    compras["b_5"].grid_forget()
    compras["b_6"].grid_forget()
    compras["b_7"].grid_forget()
    compras["b_8"].grid_forget()
    compras["img_1"].grid_forget()
    compras["img_2"].grid_forget()
    compras["img_3"].grid_forget()
    compras["img_4"].grid_forget()
    compras["p_1"].grid_forget()
    compras["p_2"].grid_forget()
    compras["p_3"].grid_forget()
    compras["p_4"].grid_forget()
    compras["t_1"].grid_forget()
    compras["b_9"].grid_forget()

    if "b_2" in pagamentos: 
        pagamentos["b_2"].grid_forget()
    if "b_3" in pagamentos: 
        pagamentos["b_3"].grid_forget()
    if "b_4" in pagamentos: 
        pagamentos["b_4"].grid_forget()
    if "c" in pagamentos: 
        pagamentos["c"].grid_forget()
    if "p_1" in pagamentos: 
        pagamentos["p_1"].grid_forget()
    if "p_2" in pagamentos: 
        pagamentos["p_2"].grid_forget()
    if "p_3" in pagamentos:
        pagamentos["p_3"].grid_forget()
    if "t_1" in pagamentos: 
        pagamentos["t_1"].grid_forget()
    if "t_2" in pagamentos: 
        pagamentos["t_2"].grid_forget()
    if "t_3" in pagamentos: 
        pagamentos["t_3"].grid_forget()
    if "t_4" in pagamentos: 
        pagamentos["t_4"].grid_forget()
    if "b_1" in pagamentos:
        pagamentos["b_1"].grid_forget()
    

def login():
    
    if entrada1.get() in usuarios:
        if usuarios[entrada1.get()].senha == entrada2.get():
            #usuarios[entrada1.get()] = Usuario(entrada2.get(), entrada1.get())
            texto.config(text=f"Bem vindo de volta {usuarios[entrada1.get()].cara}")
            compras["t_1"] = ap.Label(aba2, text="Esses são nossos produtos", background="#5F5F5F", fg="#FF8800")
            compras["t_1"].grid(row=2,column=2, columnspan=2, padx=10,pady=10)

            compras["b_9"] = ap.Button(aba1, text="SAIR", command=logaut, bg="#ff0000", fg="#9bf2f5")
            compras["b_9"].grid(row=4,column=2, padx=10,pady=10)

            produto.config(text=f"{motor.produdo} com {motor.estoque} no estoque")
            produto.grid(row=3,column=1,padx=10,pady=10)
            compras["p_1"] = ap.Label(aba2, text=f"R${motor.custo}", background="#5F5F5F", fg="#FF8800")
            compras["p_1"].grid(row=4,column=1,padx=2,pady=2)
            compras["img_1"] = ap.Label(aba2, image=img_motor)
            compras["img_1"].grid(row=5,column=1, padx=10,pady=10)
            motor_selc.grid(row=6,column=1,padx=10,pady=10)
            compras["b_1"] = ap.Button(aba2, text="Retirar 1", command=sub_motor, bg="#1290f7", fg="#1fe08f")
            compras["b_1"].grid(row=7,column=1, padx=10,pady=10)
            compras["b_2"] = ap.Button(aba2, text="Adicionar 1", command=add_motor, bg="#3dfc56", fg="#321fe0")
            compras["b_2"].grid(row=8,column=1, padx=10,pady=10)

            produto2.config(text=f"{supercharger.produdo} com {supercharger.estoque} no estoque")
            produto2.grid(row=3,column=2,padx=10,pady=10)
            compras["p_2"] = ap.Label(aba2, text=f"R${supercharger.custo}", background="#5F5F5F", fg="#FF8800")
            compras["p_2"].grid(row=4,column=2,padx=2,pady=2)
            compras["img_2"] = ap.Label(aba2, image=img_charge)
            compras["img_2"].grid(row=5,column=2, padx=10,pady=10)
            charge_selc.grid(row=6,column=2,padx=10,pady=10)
            compras["b_3"] = ap.Button(aba2, text="Retirar 1", command=sub_supercharger, bg="#1290f7", fg="#1fe08f")
            compras["b_3"].grid(row=7,column=2, padx=10,pady=10)
            compras["b_4"] = ap.Button(aba2, text="Adicionar 1", command=add_supercharger, bg="#3dfc56", fg="#321fe0")
            compras["b_4"].grid(row=8,column=2, padx=10,pady=10)

            '''texto2.config(text=f"Seja bem vindo {usuarios[entrada1.get()].cara}")
            compras["t_2"] = ap.Label(aba2_2, text="Esses são nossos produtos", background="#5F5F5F", fg="#FF8800").grid(row=2,column=2,padx=10,pady=10)'''

            produto3.config(text=f"{bom_d_agua.produdo} com {bom_d_agua.estoque} no estoque")
            produto3.grid(row=3,column=3,padx=10,pady=10)
            compras["p_3"] = ap.Label(aba2, text=f"R${bom_d_agua.custo}", background="#5F5F5F", fg="#FF8800")
            compras["p_3"].grid(row=4,column=3,padx=2,pady=2)
            compras["img_3"] = ap.Label(aba2, image=img_bom_d_agua)
            compras["img_3"].grid(row=5,column=3, padx=10,pady=10)
            bomb_d_agua_selc.grid(row=6, column=3, padx=10,pady=10)
            compras["b_5"] = ap.Button(aba2, text="Retirar 1", command=sub_bom_d_agua, bg="#1290f7", fg="#1fe08f")
            compras["b_5"].grid(row=7,column=3, padx=10,pady=10)
            compras["b_6"] = ap.Button(aba2, text="Adicionar 1", command=add_bom_d_agua, bg="#3dfc56", fg="#321fe0")
            compras["b_6"].grid(row=8,column=3, padx=10,pady=10)

            produto4.config( text=f"{bom_oleo.produdo} com {bom_oleo.estoque} no estoque")
            produto4.grid(row=3,column=4,padx=10,pady=10)
            compras["p_4"] = ap.Label(aba2, text=f"R${bom_oleo.custo}", background="#5F5F5F", fg="#FF8800")
            compras["p_4"].grid(row=4,column=4,padx=2,pady=2)
            compras["img_4"] = ap.Label(aba2, image=img_bom_oleo)
            compras["img_4"].grid(row=5,column=4, padx=10,pady=10)
            bomb_oleo_selc.grid(row=6, column=4, padx=10,pady=10)
            compras["b_7"] = ap.Button(aba2, text="Retirar 1", command=sub_bom_oleo, bg="#1290f7", fg="#1fe08f")
            compras["b_7"].grid(row=7,column=4, padx=10,pady=10)
            compras["b_8"] = ap.Button(aba2, text="Adicionar 1", command=add_bom_oleo, bg="#3dfc56", fg="#321fe0")
            compras["b_8"].grid(row=8,column=4, padx=10,pady=10)


            texto2.config(text="Aperte o botão para ver o total")
            pagamentos["b_1"] = ap.Button(aba3, text="Mostrar Total", command=show_total, bg="#3d5afc", fg="#1fe0e0")
            pagamentos["b_1"].grid(row=2,column=2, padx=10, pady=10)
        else:
            messagebox.showinfo("Error", "Senha invalida, insira a senha novamente")

    else:
        usuarios[entrada1.get()] = Usuario(entrada2.get(), entrada1.get())
        texto.config(text=f"Seja bem vindo {usuarios[entrada1.get()].cara}")
        compras["t_1"] = ap.Label(aba2, text="Esses são nossos produtos", background="#5F5F5F", fg="#FF8800")
        compras["t_1"].grid(row=2,column=2, columnspan=2, padx=10,pady=10)

        compras["b_9"] = ap.Button(aba1, text="SAIR", command=logaut, bg="#ff0000", fg="#9bf2f5")
        compras["b_9"].grid(row=4,column=2, padx=10,pady=10)

        produto.config(text=f"{motor.produdo} com {motor.estoque} no estoque")
        produto.grid(row=3,column=1,padx=10,pady=10)
        compras["p_1"] = ap.Label(aba2, text=f"R${motor.custo}", background="#5F5F5F", fg="#FF8800")
        compras["p_1"].grid(row=4,column=1,padx=2,pady=2)
        compras["img_1"] = ap.Label(aba2, image=img_motor)
        compras["img_1"].grid(row=5,column=1, padx=10,pady=10)
        motor_selc.grid(row=6,column=1,padx=10,pady=10)
        compras["b_1"] = ap.Button(aba2, text="Retirar 1", command=sub_motor, bg="#1290f7", fg="#1fe08f")
        compras["b_1"].grid(row=7,column=1, padx=10,pady=10)
        compras["b_2"] = ap.Button(aba2, text="Adicionar 1", command=add_motor, bg="#3dfc56", fg="#321fe0")
        compras["b_2"].grid(row=8,column=1, padx=10,pady=10)

        produto2.config(text=f"{supercharger.produdo} com {supercharger.estoque} no estoque")
        produto2.grid(row=3,column=2,padx=10,pady=10)
        compras["p_2"] = ap.Label(aba2, text=f"R${supercharger.custo}", background="#5F5F5F", fg="#FF8800")
        compras["p_2"].grid(row=4,column=2,padx=2,pady=2)
        compras["img_2"] = ap.Label(aba2, image=img_charge)
        compras["img_2"].grid(row=5,column=2, padx=10,pady=10)
        charge_selc.grid(row=6,column=2,padx=10,pady=10)
        compras["b_3"] = ap.Button(aba2, text="Retirar 1", command=sub_supercharger, bg="#1290f7", fg="#1fe08f")
        compras["b_3"].grid(row=7,column=2, padx=10,pady=10)
        compras["b_4"] = ap.Button(aba2, text="Adicionar 1", command=add_supercharger, bg="#3dfc56", fg="#321fe0")
        compras["b_4"].grid(row=8,column=2, padx=10,pady=10)

        '''texto2.config(text=f"Seja bem vindo {usuarios[entrada1.get()].cara}")
        compras["t_2"] = ap.Label(aba2_2, text="Esses são nossos produtos", background="#5F5F5F", fg="#FF8800").grid(row=2,column=2,padx=10,pady=10)'''

        produto3.config(text=f"{bom_d_agua.produdo} com {bom_d_agua.estoque} no estoque")
        produto3.grid(row=3,column=3,padx=10,pady=10)
        compras["p_3"] = ap.Label(aba2, text=f"R${bom_d_agua.custo}", background="#5F5F5F", fg="#FF8800")
        compras["p_3"].grid(row=4,column=3,padx=2,pady=2)
        compras["img_3"] = ap.Label(aba2, image=img_bom_d_agua)
        compras["img_3"].grid(row=5,column=3, padx=10,pady=10)
        bomb_d_agua_selc.grid(row=6, column=3, padx=10,pady=10)
        compras["b_5"] = ap.Button(aba2, text="Retirar 1", command=sub_bom_d_agua, bg="#1290f7", fg="#1fe08f")
        compras["b_5"].grid(row=7,column=3, padx=10,pady=10)
        compras["b_6"] = ap.Button(aba2, text="Adicionar 1", command=add_bom_d_agua, bg="#3dfc56", fg="#321fe0")
        compras["b_6"].grid(row=8,column=3, padx=10,pady=10)

        produto4.config( text=f"{bom_oleo.produdo} com {bom_oleo.estoque} no estoque")
        produto4.grid(row=3,column=4,padx=10,pady=10)
        compras["p_4"] = ap.Label(aba2, text=f"R${bom_oleo.custo}", background="#5F5F5F", fg="#FF8800")
        compras["p_4"].grid(row=4,column=4,padx=2,pady=2)
        compras["img_4"] = ap.Label(aba2, image=img_bom_oleo)
        compras["img_4"].grid(row=5,column=4, padx=10,pady=10)
        bomb_oleo_selc.grid(row=6, column=4, padx=10,pady=10)
        compras["b_7"] = ap.Button(aba2, text="Retirar 1", command=sub_bom_oleo, bg="#1290f7", fg="#1fe08f")
        compras["b_7"].grid(row=7,column=4, padx=10,pady=10)
        compras["b_8"] = ap.Button(aba2, text="Adicionar 1", command=add_bom_oleo, bg="#3dfc56", fg="#321fe0")
        compras["b_8"].grid(row=8,column=4, padx=10,pady=10)


        texto2.config(text="Aperte o botão para ver o total")
        pagamentos["b_1"] = ap.Button(aba3, text="Mostrar Total", command=show_total, bg="#3d5afc", fg="#1fe0e0")
        pagamentos["b_1"].grid(row=2,column=2, padx=10, pady=10)




img = ap.PhotoImage(file="Marcão.png")
ap.Label(aba1, image=img).grid(row=1,column=2, padx=10,pady=10)

ap.Label(aba1, text="escreva o seu nome:", background="#5F5F5F", fg="#FF8800").grid(row=2,column=1, padx=10,pady=10)
entrada1 = ap.Entry(aba1, width=30,)
entrada1.grid(row=2,column=2, padx=10,pady=10)

ap.Label(aba1, text="escreva a senha: ", background="#5F5F5F", fg="#FF8800").grid(row=3,column=1, padx=10,pady=10)
entrada2 = ap.Entry(aba1, width=30)
entrada2.grid(row=3,column=2, padx=10,pady=10)

ap.Button(aba1, text="ENTER", command=login, bg="#59ce5f", fg="#9bf2f5").grid(row=4,column=1, columnspan=2, padx=10,pady=10)




TELA.mainloop()
