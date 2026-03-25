import csv


dados_leads = "dados.csv"

#Função para salvar os dados em uma planilha csv
def salvar_csv(corretores):

    with open(dados_leads, mode='w', newline='', encoding='utf-8') as arquivo:

        campos = ["ID", "Nome", "Leads"]

        writer = csv.DictWriter(arquivo, fieldnames=campos, delimiter=";")

        writer.writeheader()

        for id_corretor, dados in corretores.items():
            writer.writerow({"ID": id_corretor, "Nome": dados["nome"], "Leads": dados["Leads"]})

