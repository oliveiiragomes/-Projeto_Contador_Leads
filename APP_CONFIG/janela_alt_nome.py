import tkinter as tk
from tkinter import messagebox

#Aba de alteração de nome do corretor dentro do sistema. 
def janela_alteração(corretores, entry_id_operacao):

    #Criando a interface de alteração
    janela_2 = tk.Toplevel()
    janela_2.title("Painel de Alteração")
    janela_2.config(bg="dark slate gray")
    janela_2.geometry("300x300")

    #Texto que ficará acima do campo de entrada para alteração do nome. 
    qual_nome = tk.Label(janela_2, text="Insira o nome para alteração")   
    qual_nome.pack(pady=2)

    #Campo de entrada de dados que irá receber o nome para alteração. 
    inserir_nome = tk.Entry(janela_2)
    inserir_nome.pack(pady=2) 

    #Aqui estou coletando o ID que será inserido no campo de entrada de dados "entry_id_operacao".
    id_nome = entry_id_operacao.get().strip()
    
    #Verifica se o ID foi preenchido corretamente, se não for preenchido irá fechar a janela de alteração.
    if not id_nome:
        messagebox.showwarning("Atenção", "Insira o número do ID do corretor")
        return janela_2.destroy()
    
    #Valida se o ID existe dentro do sistema, se não existir irá fechar a janela de alteração.
    if id_nome not in corretores:
        messagebox.showwarning("Atenção", "ID não encontrado!")
        return janela_2.destroy()
    
    #Função para alterar o nome. 
    def alterar_nome():
        global nome_alterar
        nome_alterar = inserir_nome.get().strip() #Coleta de dados, salva o valor do campo "inserir_nome" na variavel "nome_alterar"
        
        # Valida se o campo de nome para alteração não esta vazio
        if not nome_alterar:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return
        else:
            corretores[id_nome] = {"nome": nome_alterar, "Leads": 0}
            messagebox.showwarning("Sucesso!", "Nome alterado!")
            janela_2.destroy()

    #Botão que irá chamar a função de alteração, assim que for clicado será alterado o nome no sistema. 
    btn_alterar_nome = tk.Button(janela_2, text="Alterar nome", command=alterar_nome)
    btn_alterar_nome.pack(pady=2)

