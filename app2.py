#python
# Importa o módulo random para seleção aleatória de palavras
import random

# Lista de palavras para o jogo (banco de palavras)
palavras = ['maçã', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    """
    Função principal que gerencia toda a lógica do jogo da forca:
    - Seleção da palavra
    - Controle de tentativas
    - Validação das letras
    - Exibição do estado do jogo
    """
    
    # Seleciona aleatoriamente uma palavra da lista
    palavra_secreta = random.choice(palavras)
    
    # Lista para armazenar as letras descobertas (inicialmente todas ocultas)
    letras_corretas = ['_'] * len(palavra_secreta)
    
    # Lista para registrar letras incorretas digitadas
    letras_erradas = []
    
    # Define o número máximo de tentativas permitidas
    tentativas_restantes = 6

    # Mensagem inicial do jogo
    print("\nBem-vindo ao jogo da forca!")
    print(f"Você tem {tentativas_restantes} tentativas para adivinhar a palavra.\n")

    # Loop principal do jogo: continua enquanto houver tentativas e letras faltando
    while tentativas_restantes > 0 and '_' in letras_corretas:
        # Exibe o progresso atual do jogador
        print(' '.join(letras_corretas))
        
        # Solicita e processa a tentativa do jogador
        tentativa = input("\nDigite uma letra: ").lower()  # Converte para minúscula
        
        # Verifica se a letra está na palavra secreta
        if tentativa in palavra_secreta:
            # Atualiza as letras corretas reveladas
            for indice, letra in enumerate(palavra_secreta):
                if letra == tentativa:
                    letras_corretas[indice] = tentativa
        else:
            # Trata letra incorreta
            letras_erradas.append(tentativa)  # Registra a tentativa errada
            tentativas_restantes -= 1         # Reduz o número de tentativas
            
            # Feedback imediato para o jogador
            print(f"\nLetra incorreta! Tentativas restantes: {tentativas_restantes}")
            if letras_erradas:  # Só mostra se houver letras erradas
                print(f"Letras erradas: {', '.join(letras_erradas)}")

    # Verificação final do resultado do jogo
    if '_' not in letras_corretas:
        # Vitória: todas as letras foram reveladas
        print(f"\nParabéns! Você ganhou! A palavra era: {palavra_secreta}")
    else:
        # Derrota: acabaram as tentativas
        print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")

# Inicia o jogo quando o script é executado
if __name__ == "__main__":
    jogo_da_forca()