import os
import pyaes

# Passo 1: abrir o arquivo criptografado
file_name = "arquivo.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## Passo 2: remover o arquivo criptografado
os.remove(file_name)

## Passo 3: criar o arquivo descriptografado
new_file = "arquivo.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()