import json

def escrever_json(arquivo, dados):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def ler_json(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return None

pessoa = {
    "nome": "Talyta Sampaio",
    "idade": 29,
    "cidade": "Manaus"
}
arquivo_json = "dados_pessoa.json"

escrever_json(arquivo_json, pessoa)

dados_lidos = ler_json(arquivo_json)
if dados_lidos:
    print("Dados lidos do JSON:")
    print(dados_lidos)