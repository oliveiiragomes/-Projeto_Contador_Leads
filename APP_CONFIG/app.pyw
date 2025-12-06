import tkinter as tk
from tkinter import messagebox
import os
import csv



#Dicionário para armazenar os ID's e Nomes dos corretores
corretores = {}

#Função para cadastrar corretor
def cadastrar_corretor():


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


#Aba de alteração de nome do corretor dentro do sistema. 
def janela_alteração():

    #Criando a interface de alteração
    janela_2 = tk.Tk()
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


    
# Função para adicionar lead ao corretor
def adicionar_lead():
    id_corretor = entry_id_operacao.get().strip() #Salva o valor do campo de entrada de dados "entry_id_operacao" na variavel "id_corretor".

    #Verifica se o corretor esta dentro do sistema pelo ID.
    if id_corretor in corretores:
        corretores[id_corretor]["Leads"] += 1
        messagebox.showinfo("Sucesso", "Lead adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Corretor não encontrado!")





# Função para remover lead do corretor
def remover_lead():
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





# Função para listar todos os corretores
def listar_corretores():
    
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


#Função para salvar os dados em uma planilha csv
def salvar_csv():
    global dados_leads
    dados_leads = "dados.csv"

    with open(dados_leads, mode='w', newline='', encoding='utf-8') as arquivo:

        campos = ["ID", "Nome", "Leads"]

        writer = csv.DictWriter(arquivo, fieldnames=campos, delimiter=";")

        writer.writeheader()

        for id_corretor, dados in corretores.items():
            writer.writerow({"ID": id_corretor, "Nome": dados["nome"], "Leads": dados["Leads"]})



# Criando a janela principal
janela = tk.Tk()
janela.title("Titulo da página")
janela.config(bg="DarkBlue")
janela.geometry("500x700")

#Importando imagem da logo
imagem = tk.PhotoImage(file="APP_CONFIG/images_lead_control.png")

#Aqui estou exibindo a imagem na tela
label = tk.Label(janela, image=imagem, borderwidth="2px") 
label.pack(side="top")




# ==== Seção de Cadastro de Corretor ==== #

#Aqui é adicionado o texto que ficará por cima do campo de entrada de dados
tk.Label(janela, text="ID do Corretor").pack() 

#A função "tk.ENTRY" cria o campo de entrada de dados do ID
entry_id = tk.Entry(janela, borderwidth="2px") 
#Aqui estou centralizando essa campo de entrada de dados  do ID
entry_id.pack(side="top", pady=(1, 10)) 

#Aqui é adicionado o texto que ficará por cima do campo de entrada de dados 
tk.Label(janela, text="Nome do Corretor").pack() 

#Aqui eu criei o campo de entrada de dados, colocando uma borda 
entry_nome = tk.Entry(janela, borderwidth="2px")
# Aqui estou centralizando o campo de entrada de dados do nome
entry_nome.pack(side="top", pady=(1, 0)) 


#Aqui eu criei o botão para cadastrar nome do corretor no sistema. 
btn_cadastrar = tk.Button(janela, text="Cadastrar Corretor", command=cadastrar_corretor)
btn_cadastrar.pack(side="top", pady=(10, 25))



# ==== Seção de Operações com Leads ====

#Criando uma label como titulo para indicar que o campo abaixo sera para inserção do id do corretor para fazer a operação desejada.
tk.Label(janela, text="ID do Corretor para Operações").pack()
#Aqui estou criando o campo de entrada de dados para realizar as operações(add lead, rem lead).
entry_id_operacao = tk.Entry(janela, borderwidth="2px")
entry_id_operacao.pack(side="top", pady=(1, 0))

#Aqui estou criando o botão para adicionar lead, quando clicado, chamará a função "adicionar_lead".
btn_adicionar = tk.Button(janela, text="Adicionar Lead", command=adicionar_lead)
btn_adicionar.pack(pady=2)

#Aqui estou criando o botão para remover lead, quando clicado, chamará a função "remover_lead".
btn_remover = tk.Button(janela, text="Remover Lead", command=remover_lead)
btn_remover.pack(pady=2)

#Aqui eu crio o botão para alterar nome.
btn_alterar = tk.Button(janela, text="Alterar Nome", command= janela_alteração)
btn_alterar.pack(pady=2)



# ==== Seção de Listagem ====
btn_listar = tk.Button(janela, text="Listar Corretores", command=listar_corretores)
btn_listar.pack(pady=10)




# Campo de texto para exibir os corretores e seus leads
text_area = tk.Text(janela, height=10, width=60)
text_area.pack()




# Inicia o loop da interface
janela.mainloop()





#Chamar a função para salvar o csv
salvar_csv()


if os.name == 'nt':  # Para Windows
    os.startfile(dados_leads)



