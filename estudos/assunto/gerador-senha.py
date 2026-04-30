"""
*******************************************************************************
* DESCRIÇÃO: 
* Gerador de senhas seguras e aleatórias com critérios de força.
* 
* FUNCIONAMENTO:
* 1. Entrada: O usuário define o comprimento da senha (mínimo de 8 caracteres).
* 2. Garantia: O script força a inclusão de pelo menos uma letra maiúscula, 
*    uma minúscula, um número e um símbolo especial.
* 3. Aleatoriedade: Utiliza criptografia de nível de sistema para gerar os caracteres.
* 4. Embaralhamento: As classes de caracteres são misturadas para evitar padrões.
* 
* O QUE CONTÉM NESTE CÓDIGO:
* - Módulo 'secrets': Uso de geradores de números aleatórios seguros para criptografia.
* - Módulo 'string': Manipulação de constantes ASCII para compor a base da senha.
* - List Comprehension: Criação eficiente da lista de caracteres restantes.
* - Tratamento de Erros: Bloco try/except para validar se a entrada é um número inteiro.
* - Estrutura de Loop (while): Garante que o programa continue rodando até uma entrada válida.
* 
* Autor/User: Amanda-Aziz
* Data: 30 de Abril de 2026
*******************************************************************************
"""

import secrets
import string

def gerar_senha(tamanho=12):
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation
    todos = maiusculas + minusculas + numeros + simbolos

    senha = [
        secrets.choice(maiusculas),
        secrets.choice(minusculas),
        secrets.choice(numeros),
        secrets.choice(simbolos)
    ]

    senha += [secrets.choice(todos) for _ in range(tamanho - 4)]
    secrets.SystemRandom().shuffle(senha)
    return ''.join(senha)

print("\n============================================")
print("DICA: Senhas maiores (8 a 12+ caracteres)")
print("são muito mais seguras!")
print("============================================")

if __name__ == "__main__":
    # para o programa não encerrar
    while True:
        try:
            tamanho_entrada = input("\nDigite o tamanho desejado para a senha: ")
            tamanho_da_senha = int(tamanho_entrada)

            if tamanho_da_senha < 8:
                print("\nErro: Por segurança, escolha um tamanho")
                print("de pelo menos 8 caracteres.")
                
                continue  # voltar ao início do input
            
            senha_segura = gerar_senha(tamanho_da_senha)
            print("\n============================================")
            print("\nSenha gerada:", senha_segura)

            break
            
        except ValueError:
            print("\nErro: Digite apenas números inteiros (ex: 12, 50).")

print("\n============================================")
