from tkinter import messagebox


# Função para remover lead do corretor
def remover_lead(entry_id_operacao, corretores):
    id_corretor = entry_id_operacao.get().strip() #Coleta de dados

    '''
    Primeiramente verifica se o ID está cadastrado no sistema;
    Segundamente verifica se o corretor tem leads para remover, se o valor em "corretores[id_corretor]["Leads"]" 
    for maior que 0, será removido 1 lead.
    '''
    if id_corretor in corretores:
        if corretores[id_corretor]["Leads"] > 0:
            corretores[id_corretor]["Leads"] -= 1
            messagebox.showinfo("Sucesso", "Lead removido com sucesso!")
        else:
            messagebox.showwarning("Atenção", "Este corretor não possui leads!")
    else:
        messagebox.showerror("Erro", "Corretor não encontrado!")