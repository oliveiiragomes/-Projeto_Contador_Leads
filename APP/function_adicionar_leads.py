from tkinter import messagebox


# Função para adicionar lead ao corretor
def adicionar_lead(entry_id_operacao, corretores):
    
    #Salva o valor do campo de entrada de dados "entry_id_operacao" na variavel "id_corretor".
    id_corretor = entry_id_operacao.get().strip() 
    
    #Verifica se o corretor esta dentro do sistema pelo ID.
    if id_corretor in corretores:
        corretores[id_corretor]["Leads"] += 1
        messagebox.showinfo("Sucesso", "Lead adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Corretor não encontrado!")