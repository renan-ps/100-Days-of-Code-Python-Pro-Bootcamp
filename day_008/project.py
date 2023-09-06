# Definindo uma lista de caracteres do alfabeto
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# Inicializando uma variável para controlar a execução do programa
cont = True


# Função para realizar a cifra de César
def caesar(text, shift, direction):
    # Verificando se a operação é de decodificação
    if direction == "decode":
        shift *= -1

    # Inicializando uma variável para armazenar o texto cifrado ou decifrado
    finalText = ""

    # Iterando através dos caracteres do texto de entrada
    for char in text:
        # Verificando se o caractere está no alfabeto
        if char in alphabet:
            # Obtendo a posição do caractere no alfabeto
            position = alphabet.index(char)
            # Calculando a nova posição usando o deslocamento e aplicando a aritmética modular para garantir que esteja dentro do alfabeto
            newPosition = (position + shift) % 26
            # Adicionando o caractere correspondente à nova posição ao texto final
            finalText += alphabet[newPosition]
        else:
            # Se o caractere não estiver no alfabeto, mantenha-o inalterado
            finalText += char

    # Imprimindo o resultado
    print(f"Resultado: {finalText}")


# Iniciando um loop que permite ao usuário continuar ou sair do programa
while cont:
    # Solicitando ao usuário a escolha entre codificar ou decodificar
    direction = input(
        "Digite 'encode' para encriptar e 'decode' para decriptar:\n")
    # Solicitando ao usuário a mensagem de entrada em letras minúsculas
    text = input("Digite a mensagem:\n").lower()
    # Solicitando ao usuário o número de posições para deslocamento
    shift = int(input("Digite o número de posições:\n"))

    # Chamando a função caesar para processar a mensagem
    caesar(text, shift, direction)

    # Perguntando ao usuário se deseja continuar
    restart = input("Deseja continuar? (sim ou não)\n").lower()
    if restart == "não":
        cont = False
        print("Até mais!")
