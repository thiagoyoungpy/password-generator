import random
import string

print("thiagoyoungpy ©")

def gerar_senha(complexidade, tamanho):
    caracteres = ""

    if complexidade >= 1:
        caracteres += string.ascii_lowercase
    if complexidade >= 2:
        caracteres += string.ascii_uppercase
    if complexidade >= 3:
        caracteres += string.digits
    if complexidade >= 4:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

senhas = int(input("Number of password(s) you want to generate: "))
complexidade = int(input("Difficulty of password(s) you want [1], [2], [3], [4]: "))
tamanho = int(input("Length of the password(s) you want to generate: "))

for _ in range(senhas):
    senha_gerada = gerar_senha(complexidade, tamanho)
    print("Senha(s) gerada(s):", senha_gerada)
    
input("Press enter for exit.")