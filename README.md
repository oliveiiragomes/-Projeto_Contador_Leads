# -Projeto_Contador_Leads

Este é um aplicativo desktop simples desenvolvido em Python com Tkinter para o gerenciamento de corretores e controle de leads. O sistema permite cadastrar profissionais, atribuir ou remover leads e exportar os dados automaticamente para uma planilha CSV ao fechar a aplicação.

## 📋 Funcionalidades

* **Cadastro de Corretores:** Registro de novos corretores com ID e Nome.
* **Controle de Leads:** Adição e remoção de leads para corretores cadastrados (via ID).
* **Edição:** Alteração de nome de corretores existentes através de um painel dedicado.
* **Listagem:** Visualização rápida de todos os corretores e seus respectivos saldos de leads.
* **Exportação Automática:** Ao fechar o aplicativo, os dados são salvos em `dados.csv` e o arquivo é aberto automaticamente (no Windows).

## 🛠️ Pré-requisitos

* **Python 3.x** instalado.
* Biblioteca **Tkinter** (geralmente já vem instalada com o Python).
* Sistema Operacional Windows (para a funcionalidade de abertura automática do CSV).
