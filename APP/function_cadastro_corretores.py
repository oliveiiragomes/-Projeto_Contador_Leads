import tkinter as tk
from tkinter import messagebox



#Função para cadastrar corretor
def cadastrar_corretor(entry_id, entry_nome, corretores):
    id_corretor = entry_id.get().strip()  # Pega o ID do campo de texto
    nome = entry_nome.get().strip()       # Pega o nome do campo de texto


    #Valida se os campos não estão vazios
    if not id_corretor or not nome:
        messagebox.showwarning("Atenção", "Preencha todos os campos!")
        return

    #Verifica se o ID já está cadastrado
    if id_corretor not in corretores:
        #Adiciona corretor ao vetor
        corretores[id_corretor] = {"nome": nome, "Leads": 0}
        messagebox.showinfo("Sucesso", f"Corretor {nome} cadastrado!")
    else:
        messagebox.showerror("Erro", "ID já cadastrado!")



    #Limpa os campos após cadastro
    entry_id.delete(0, tk.END)
    entry_nome.delete(0, tk.END)
    