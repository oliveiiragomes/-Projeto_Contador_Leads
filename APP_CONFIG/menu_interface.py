import tkinter as tk
from tkinter import messagebox
import os
import csv
from function_cadastro_corretores import cadastrar_corretor
from function_adicionar_leads import adicionar_lead
from function_remover_lead import remover_lead
from function_listar_corretores import listar_corretores



#Dicionário para armazenar os ID's e Nomes dos corretores
corretores = {}




#Aba de alteração de nome do corretor dentro do sistema. 
def janela_alteração():

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



#Aqui estou criando a tela principal do sistema
janela = tk.Tk()
janela.title("Título da Página")
janela.config(bg="DarkBlue")
janela.geometry("500x800")



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
btn_cadastrar = tk.Button(janela, text="Cadastrar Corretor", command=lambda: cadastrar_corretor(entry_id, entry_nome, corretores))
btn_cadastrar.pack(side="top", pady=(10, 25))



# ==== Seção de Operações com Leads ====

#Criando uma label como titulo para indicar que o campo abaixo sera para inserção do id do corretor para fazer a operação desejada.
tk.Label(janela, text="ID do Corretor para Operações").pack()
#Aqui estou criando o campo de entrada de dados para realizar as operações(add lead, rem lead).
entry_id_operacao = tk.Entry(janela, borderwidth="2px")
entry_id_operacao.pack(side="top", pady=(1, 0))

#Aqui estou criando o botão para adicionar lead, quando clicado, chamará a função "adicionar_lead".
btn_adicionar = tk.Button(janela, text="Adicionar Lead", command=lambda: adicionar_lead(entry_id_operacao, corretores))
btn_adicionar.pack(pady=2)

#Aqui estou criando o botão para remover lead, quando clicado, chamará a função "remover_lead".
btn_remover = tk.Button(janela, text="Remover Lead", command=lambda: remover_lead(entry_id_operacao, corretores))
btn_remover.pack(pady=2)

#Aqui eu crio o botão para alterar nome.
btn_alterar = tk.Button(janela, text="Alterar Nome", command= janela_alteração)
btn_alterar.pack(pady=2)


#Aqui crio um botão para salvar o arquivo CSV 
btn_salvar_csv = tk.Button(janela, text="Salvar CSV", command= salvar_csv)
btn_salvar_csv.pack(pady=2)


# ==== Seção de Listagem ====
btn_listar = tk.Button(janela, text="Listar Corretores", command=lambda: listar_corretores(text_area, corretores))
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


