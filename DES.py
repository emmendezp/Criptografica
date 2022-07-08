import pyDes
import base64


def main():
    print("****************Cifrado DES***************")
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
    key = input("-Ingrese la Key -> ")
    print("-El archivo en base64 es -> ", b64image)

    k = pyDes.des(key.encode(),pyDes.CBC, b"\0\1\0\1\0\1\0\0", pad=None,padmode=pyDes.PAD_PKCS5)
    encriptada = k.encrypt(b64image)

    print("-Archivo cifrado : " , encriptada)
    encriptada64= base64.b64encode(encriptada)
    print("archivo base 64 encriptado",encriptada64)
    image= open(""+archivo, "wb")
    image.write(base64.b64decode(encriptada64))
    image.close()
    print("Guardado como ",""+archivo)

def Descifrar():
    archivo = input("-Ingrese Nombre del la Imagen -> ")
    key = input("-Ingrese la Key -> ")
    with open(archivo, "rb") as img_file:
        b64image2 = base64.b64encode(img_file.read())
    print("-Archivo leido en base 64 ->",b64image2)

    desencriptada = base64.b64decode(b64image2)

    k = pyDes.des(key.encode(),pyDes.CBC, b"\0\1\0\1\0\1\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    desencriptada = k.decrypt(desencriptada)
    print("-archivo descrifrado en base 64",desencriptada)
    image= open(""+archivo, "wb")

    image.write(base64.b64decode(desencriptada))
    image.close()
    print("Guardado como ",""+archivo)

if __name__ == "__main__":
    main()