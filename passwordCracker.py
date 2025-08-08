import zipfile

zip_file = 'Secret.zip'

diccionario = "rockyou.txt"

with zipfile.ZipFile(zip_file, 'r') as zf:
    with open(diccionario, 'r', errors='ignore') as f:
        for linea in f:
             password = linea.strip()
             try:
                 zip.extractall(pwd=bytes(password, 'utf-8'))
                 print(f"Contraseña Crackeada: {password}")
                 break
             except:
                 pass