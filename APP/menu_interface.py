import tkinter as tk
from tkinter import messagebox
import os
from janela_alt_nome import janela_alteração
from function_salvar_csv import salvar_csv, dados_leads
from function_cadastro_corretores import cadastrar_corretor
from function_adicionar_leads import adicionar_lead
from function_remover_lead import remover_lead
from function_listar_corretores import listar_corretores
from dict_corretores import corretores


#Aqui estou criando a tela principal do sistema
janela = tk.Tk()
janela.title("Título da Página")
janela.config(bg="gray20")
janela.geometry("1000x800")

# Frame principal para centralizar conteúdo
frame_principal = tk.Frame(janela, bg="gray20")
frame_principal.pack(expand=True, fill="both", padx=20, pady=20)

#Importando imagem da logo 
imagem = tk.PhotoImage(file="APP_CONFIG/images_lead_control.png")
#Aqui estou exibindo a imagem na tela
imagem_import = tk.Label(frame_principal, image=imagem, borderwidth="2px", bg="gray20") 
imagem_import.pack(side="top", pady=(0, 20))

# ==== Seção de Cadastro de Corretor ==== #
frame_cadastro = tk.Frame(frame_principal, bg="gray20")
frame_cadastro.pack(side="top", pady=(0, 20))

#Aqui é adicionado o texto que ficará por cima do campo de entrada de dados
tk.Label(frame_cadastro, text="ID do Corretor", bg="gray20", fg="white").pack(pady=(0, 5)) 

#A função "tk.ENTRY" cria o campo de entrada de dados do ID
entry_id = tk.Entry(frame_cadastro, borderwidth="2px") 
#Aqui estou centralizando essa campo de entrada de dados  do ID
entry_id.pack(pady=(0, 10)) 

#Aqui é adicionado o texto que ficará por cima do campo de entrada de dados 
tk.Label(frame_cadastro, text="Nome do Corretor", bg="gray20", fg="white").pack(pady=(0, 5)) 

#Aqui eu criei o campo de entrada de dados, colocando uma borda 
entry_nome = tk.Entry(frame_cadastro, borderwidth="2px")
# Aqui estou centralizando o campo de entrada de dados do nome
entry_nome.pack(pady=(0, 10)) 

#Aqui eu criei o botão para cadastrar nome do corretor no sistema. 
btn_cadastrar = tk.Button(frame_cadastro, text="Cadastrar Corretor", command=lambda: cadastrar_corretor(entry_id, entry_nome, corretores))
btn_cadastrar.pack(pady=(0, 10))

# ==== Seção de Operações com Leads ==== #
frame_operacoes = tk.Frame(frame_principal, bg="gray20")
frame_operacoes.pack(side="top", pady=(0, 20))

#Criando uma label como titulo para indicar que o campo abaixo sera para inserção do id do corretor para fazer a operação desejada.
tk.Label(frame_operacoes, text="ID do Corretor para Operações", bg="gray20", fg="white").pack(pady=(0, 5))
#Aqui estou criando o campo de entrada de dados para realizar as operações(add lead, rem lead).
entry_id_operacao = tk.Entry(frame_operacoes, borderwidth="2px")
entry_id_operacao.pack(pady=(0, 10))

# Frame para os botões de operações
frame_botoes_operacoes = tk.Frame(frame_operacoes, bg="gray20")
frame_botoes_operacoes.pack()

#Aqui estou criando o botão para adicionar lead, quando clicado, chamará a função "adicionar_lead".
btn_adicionar = tk.Button(frame_botoes_operacoes, text="Adicionar Lead", command=lambda: adicionar_lead(entry_id_operacao, corretores))
btn_adicionar.pack(side="left", padx=5)

#Aqui estou criando o botão para remover lead, quando clicado, chamará a função "remover_lead".
btn_remover = tk.Button(frame_botoes_operacoes, text="Remover Lead", command=lambda: remover_lead(entry_id_operacao, corretores))
btn_remover.pack(side="left", padx=5)

#Aqui eu crio o botão para alterar nome.
btn_alterar = tk.Button(frame_botoes_operacoes, text="Alterar Nome", command=lambda: janela_alteração(corretores, entry_id_operacao))
btn_alterar.pack(side="left", padx=5)

#Aqui crio um botão para salvar o arquivo CSV 
btn_salvar_csv = tk.Button(frame_botoes_operacoes, text="Salvar CSV", command=lambda: salvar_csv(corretores))
btn_salvar_csv.pack(side="left", padx=5)

# ==== Seção de Listagem ====
frame_listagem = tk.Frame(frame_principal, bg="gray20")
frame_listagem.pack(side="top", pady=(0, 20))

btn_listar = tk.Button(frame_listagem, text="Listar Corretores", command=lambda: listar_corretores(text_area, corretores))
btn_listar.pack(pady=(0, 10))

# Campo de texto para exibir os corretores e seus leads
text_area = tk.Text(frame_listagem, height=10, width=60)
text_area.pack()


# Inicia o loop da interface

janela.mainloop()
    
    #Chamar a função para salvar o csv
salvar_csv(corretores)
    
if os.name == 'nt':  # Para Windows
    os.startfile(dados_leads)


