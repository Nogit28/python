from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from flor import Flor
from flor_dao import FlorDao

global novo
novo = True
f1 = Flor()
fdao = FlorDao()

def habilitar():
  txtcodigo.configure(state="normal")
  txtdesc.configure(state="normal")
  cbounidade.configure(state="normal")
  txtquantidade.configure(state="normal")
  txtpreco.configure(state="normal")
  btncancelar.configure(state="normal")
  btnsalvar.configure(state="normal")
  btnnovo.configure(state="disabled")

def desabilitar():
  txtcodigo.configure(state="disabled")
  txtdesc.configure(state="disabled")
  cbounidade.configure(state="disabled")
  txtquantidade.configure(state="disabled")
  txtpreco.configure(state="disabled")
  btncancelar.configure(state="disabled")
  btnsalvar.configure(state="disabled")
  btnexcluir.configure(state="disabled")
  btnnovo.configure(state="normal")

def limpar():
  codigo.set("")
  desc.set("")
  unidade.set("")
  quantidade.set(0)
  preco.set(0)

def popupError(campo):
    messagebox.showwarning(title="Erro de validação",message=f"O campo {campo} é obrigatório.")

def pesquisar():
  resposta = simpledialog.askstring("Consulta:","Digite o código da flor:            ")
  flor = fdao.consultar(resposta)
  if flor:
    global novo
    novo = False
    habilitar()
    btnexcluir.configure(state="normal")
    codigo.set(flor.getCodigo())
    desc.set(flor.getDesc())
    unidade.set(flor.getUnidade())
    quantidade.set(flor.getQuantidade())
    preco.set(flor.getPreco())
    txtdesc.focus_set()
  else:
    messagebox.showerror("Erro","Código inválido!")
    txtcodigo.focus_set()

def inserir():
  habilitar()

def salvar():
  if codigo.get() == '':
    popupError("Código")
    txtcodigo.focus_set()
  elif desc.get() == '':
    popupError("Descrição")
    txtdesc.focus_set()
  elif unidade.get() == '':
    popupError("Unidade")
    cbounidade.focus_set()
  elif quantidade.get() == 0:
    popupError("Quantidade")
    txtquantidade.focus_set()
  elif preco.get() == 0:
    popupError("Preço")
    txtpreco.focus_set()
  else:
    f1.setCodigo(txtcodigo.get())
    f1.setDesc(txtdesc.get())
    f1.setUnidade(cbounidade.get())
    f1.setQuantidade(txtquantidade.get())
    f1.setPreco(txtpreco.get())
    global novo
    if novo:
      if fdao.incluir(f1):
        messagebox.showinfo(title="Sucesso",message="Cadastro realizado com sucesso!")
    else:
      if fdao.atualizar(f1):
        messagebox.showinfo(title="Sucesso",message="Dados atualizados com sucesso!")
    desabilitar()
    limpar()

def cancelar():
  limpar()
  desabilitar()

def excluir():
  resposta = messagebox.askokcancel(title="Confirmação",message="Tem certeza que gostaria de APAGAR esse registro?")
  if resposta and fdao.excluir(txtcodigo.get()):
    messagebox.showinfo(title="Sucesso",message="Registro excluído com sucesso!")
    limpar()
    desabilitar()

# Montagem da tela

win = Tk()
largura_tela = win.winfo_screenwidth()
altura_tela = win.winfo_screenheight()
largura_win = 275
altura_win = 210
pos_x = (largura_tela - largura_win)/2
pos_y = (altura_tela - altura_win)/2
win.title("Floricultura Vigor da Primavera")
win.geometry("%dx%d+%d+%d"%(largura_win,altura_win,pos_x,pos_y)) # Sempre centralizado
win.configure(bg="#dab9ff")
## Campos da tela
#Codigo
codigo = StringVar(win)
lblcodigo = Label(win,text="Código:",bg="#dab9ff").place(x=15,y=15)
txtcodigo = Entry(win,textvariable=codigo,width=10)
txtcodigo.place(x=15,y=35)
#Pesquisar
bttnpesq = Button(win,text="🔍",command=pesquisar,width=2)
bttnpesq.place(x=85,y=32)
#Descricao
desc = StringVar(win)
lbldesc = Label(win,text="Descrição:",bg="#dab9ff").place(x=15,y=60)
txtdesc = Entry(win,textvariable=desc,width=24)
txtdesc.place(x=15,y=80)
#Unidade
unidade = StringVar(win)
unidades = ["Unidade","Dúzia","Caixa c/ 50","Caixa c/ 100"]
lblunidade = Label(win,text="Unidade:",bg="#dab9ff").place(x=15,y=105)
cbounidade = ttk.Combobox(win,state="readonly",textvariable=unidade,values=unidades,width=21)
cbounidade.place(x=15,y=125)
#Quantidade
quantidade = IntVar(win)
lblquantidade = Label(win,text="Quantidade:",bg="#dab9ff").place(x=15,y=150)
txtquantidade = Entry(win,textvariable=quantidade,width=11,justify="right")
txtquantidade.place(x=15,y=170)
#Preco
preco = DoubleVar(win)
lblpreco = Label(win,text="Preço:",bg="#dab9ff").place(x=98,y=150)
txtpreco = Entry(win,textvariable=preco,width=10,justify="right")
txtpreco.place(x=100,y=170)
##Botões
btnnovo = Button(win, text="Novo", command=inserir, width=10)
btnnovo.place(x=180, y=15)
btnsalvar = Button(win, text="Salvar", command=salvar, width=10)
btnsalvar.place(x=180, y=52)
btncancelar = Button(win, text="Cancelar", command=cancelar, width=10)
btncancelar.place(x=180, y=90)
btnexcluir = Button(win, text="Excluir", command=excluir, width=10)
btnexcluir.place(x=180, y=127)
btnsair = Button(win, text="Sair", command=win.destroy, width=10)
btnsair.place(x=180, y=165)

desabilitar()
limpar()

win.mainloop()