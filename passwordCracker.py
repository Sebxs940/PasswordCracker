import zipfile

zip_file = "Secret.zip"

if (zip_file == ""):
    print(f"No se encontro el archivo {zip_file}")
else:
    pass

diccionario = "rockyou.txt"

if (diccionario == ""):
    print(f"No se encontro el diccionario {diccionario}")
else:
    pass

with zipfile.ZipFile(zip_file, 'r') as f:
    with open(diccionario, 'r', errors='ignore') as f:
        for linea in f:
             password = linea.strip()
             try:
                 zip.extractall(pwd=bytes(password, 'utf-8'))
                 print(f"Contraseña Crackeada: {password}")
                 break
             except:
                 print(f"La contraseña no pudo ser crackeada: {NameError}")