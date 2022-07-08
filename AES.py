import pyaes
import base64



def main():
    print("****************Cifrado AES***************")
    print("1. Cifrar")
    print("2. Descifrar")
    print("**********************************************")
    opcion = int(input('\n-Opcion -> '))
    
    if opcion == 1: #opcion cifrado
      cifrar()

    elif opcion == 2:#Opcion descifrado 
      Descifrar()

def cifrar():

    archivo = input("-Ingrese Nombre del la Imagen -> ")
    with open(archivo, "rb") as img_file:
        b64image = base64.b64encode(img_file.read())

    key=bytes(input("-Ingrese la clave (16, 24 o 32 carácteres para modo de operación 128 bits, 192 bits o 256 bits respectivamente)\n\nRta: "), 'utf-8')
    print("Archivo en base64: ", b64image)

    aes = pyaes.AESModeOfOperationCTR(key)
    encrypt = base64.b64encode(aes.encrypt(b64image)).decode("utf-8")
    print("Archivo cifrado: ",encrypt)
    print("Archivo cifrado en base64: ",encrypt)

    image = open(""+archivo, "wb")
    image.write(base64.b64decode(encrypt))
    image.close()
    print("Guardado como ",""+archivo)

def Descifrar():
    archivo = input("-Ingrese Nombre del la Imagen -> ")
    key=bytes(input("-Ingrese la clave (16, 24 o 32 carácteres para modo de operación 128 bits, 192 bits o 256 bits respectivamente)\n\nRta: "), 'utf-8')
    with open(archivo, "rb") as img_file:
        b64image2 = base64.b64encode(img_file.read())

    print("-Archivo leido en base 64 ->",b64image2)

    aes = pyaes.AESModeOfOperationCTR(key)
    decrypt = aes.decrypt(base64.b64decode(b64image2)).decode("utf-8")
    print("Archivo descifrado en base64: ",decrypt)

    image= open(""+archivo, "wb")
    image.write(base64.b64decode(decrypt))
    image.close()
    print("Guardado como ",""+archivo)
#"CLAVEDEPRUEBAAES_PARA_24"
if __name__ == "__main__":
    main()