def verificar_senha_forte():
    senha = input("Digite uma senha: ")
    
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False
    
    if not any(char.isdigit() for char in senha):
        print("A senha deve ter pelo menos 1 número.")
        return False
    
    print("A senha é forte!")
    return True

verificar_senha_forte()