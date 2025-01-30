# Função para inverter a string sem usar reverse
def inverter_string(s):
    # Inicializa a string invertida como vazia
    s_invertida = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        s_invertida += s[i]  # Adiciona o caractere na nova string
    
    return s_invertida

# Entrada de dados (pode ser uma string informada pelo usuário)
entrada = input("Digite uma string para inverter: ")

# Invertendo a string
resultado = inverter_string(entrada)

# Exibindo o resultado
print(f"String invertida: {resultado}")
