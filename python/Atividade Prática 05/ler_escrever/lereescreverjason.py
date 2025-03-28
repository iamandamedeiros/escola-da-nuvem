import json

arquivo_json = "dados_pessoas.json"

dados = [
    ["Nome", "Idade", "Cidade"], 
    ["Talyta", 29, "Manaus"],
    ["Lavini", 27, "São Paulo"],
    ["Debora", 26, "Fortaleza"]
]

with open(arquivo_json, "w", encoding="utf=8") as arquivo:
    json.dump(dados, arquivo, indent=4)
    print(f"Dados gravados em '{arquivo_json} com sucesso")
try:
    with open(arquivo_json, "r", encoding="utf=8") as arquivo:
        dados_lidos = json.load(arquivo)
        for pessoa in dados_lidos:
            print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, Cidade: {pessoa['Cidade']}")
        print("Dados lidos do arquivos JSON: ")
        print(json.dumps(dados_lidos, indent=4, ensure_ascii=False))
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro: arquivo JSON incorreto.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")