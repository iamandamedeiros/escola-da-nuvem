def verifica_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")
        print("A senha deve conter pelo menos 8 caracteres e ao menos um número!")
        
        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break
        
        if len(senha) < 8:
            print("Senha fraca: deve ter pelo menos 8 caracteres.")
            continue
        
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um número.")
            continue
        
        print("Senha forte e válida!")
        break
    
verifica_senha()