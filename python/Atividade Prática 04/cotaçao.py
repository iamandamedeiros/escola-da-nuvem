import requests

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    response = requests.get(url)
    dados = response.json()
    return dados

def exibir_cotacao(codigo_moeda):
    dados = obter_cotacao(codigo_moeda)
    chave = f"{codigo_moeda}BRL"
    if chave in dados:
        cotacao = dados[chave]
        print(f"\nCotação {cotacao['name']}:")
        print(f"Valor atual: R$ {cotacao['bid']}")
        print(f"Máximo: R$ {cotacao['high']}")
        print(f"Mínimo: R$ {cotacao['low']}")
        print(f"Data e hora da última atualização: {cotacao['create_date']}")
    else:
        print(f"Código de moeda '{codigo_moeda}' inválido ou não encontrado.")

if __name__ == "__main__":
    codigo_moeda = input("Informe o código da moeda desejada (ex: USD, EUR, GBP): ").upper()
    exibir_cotacao(codigo_moeda)
