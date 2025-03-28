def checar_idade(idade):
    if 0 <= idade <= 12:
        return "Criança (0-12 anos)"
    elif 13 <= idade <= 17:
        return "Adolescente (13-17 anos)"
    elif 18 <= idade <= 59:
        return "Adulto (18-59 anos)"
    elif idade >= 60:
        return "Idoso (60 anos ou mais)"
    else:
        return "Idade inválida"

idade = int(input("Digite sua idade: "))
print(checar_idade(idade))