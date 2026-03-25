import tkinter as tk

# Função para listar todos os corretores
def listar_corretores(text_area, corretores):
    
    #Limpa o conteúdo do campo de texto onde será mostrado os dados
    text_area.delete("1.0", tk.END)

    #Verifica se existem corretores cadastrados
    if not corretores:
        text_area.insert(tk.END, "Nenhum corretor cadastrado.\n")
        return

    #Mostra todos os corretores no campo de texto
    for id_corretor, dados in corretores.items():
        linha = f"ID: {id_corretor} | Nome: {dados['nome']} | Leads: {dados['Leads']}\n"
        text_area.insert(tk.END, linha)
