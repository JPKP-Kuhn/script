#utf-8
import string

with open('text.txt', 'r') as file:
    file_text = file.read().upper().replace(" ", "").rstrip()

# Troca a posição dos índices pela chave
def encrypt(text, key):
    alphabet = list(string.ascii_uppercase)
    text = list(text.upper())
    # Cria o alfabeto criptografado, se a chave for um número
    if isinstance(key, int):
        cipher_alphabet = alphabet.copy()
        for i in range(len(alphabet)): 
            cipher_alphabet[i] = alphabet[(i + key) % len(alphabet)]

        # Criptografa o texto
        for j in range(len(text)):
            if text[j] in alphabet:
                original_index = alphabet.index(text[j])
                text[j] = cipher_alphabet[original_index]
    else:
        return "Erro! A chave deve ser um número inteiro ou um texto menor do que o tamanho do alfabeto (26, sem contar os espaços)"
 
    return ''.join(text)

def decrypt(text, key):
    alphabet = list(string.ascii_uppercase)
    text = list(text.upper())
    # Cria o alfabeto criptografado, se a chave for um número
    if isinstance(key, int):
        cipher_alphabet = alphabet.copy()
        for i in range(len(alphabet)):
            cipher_alphabet[i] = alphabet[(i + key) % len(alphabet)]

        # Descriptografa o texto
        for j in range(len(text)):
            if text[j] in cipher_alphabet:
                original_index = cipher_alphabet.index(text[j])
                text[j] = alphabet[original_index]
    else:   
        return "Erro! A chave deve ser um número inteiro ou um texto menor do que o tamanho do alfabeto (26, sem contar os espaços)"

    return ''.join(text)

chave = 3
criptografado = encrypt(file_text, chave)
descriptografado = decrypt(criptografado, chave)
print(criptografado, descriptografado)
