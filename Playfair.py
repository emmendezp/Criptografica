import re
import sys 

letras ='ABCDEFGHIKLMNOPQRSTUVWXYZ'

def main():
    print("****************PLAYFAIR CYPHER***************")
    print("1. Cifrar")
    print("2. Descifrar")
    print("**********************************************")
    opcion = int(input('\n-Opcion -> '))
    if opcion == 1: #opcion cifrado
      mensaje, claveC = datos()
      texto = cifrarM(claveC, mensaje)
      print('\n', texto)

    elif opcion == 2:#Opcion descifrado 
      mensaje, clave = datos()
      texto = descifrarM(clave, mensaje)
      print('\n', texto)

def datos():
    mensaje = input('\nMensaje -> ')
    clave = input('key -> ')
    clave = re.sub('[^A-Z]','',clave.upper())

    clave = re.sub(r'[J]','I',clave)
    claveC = alfabetoSustitucion(clave)
    matriz = Mmatriz(claveC)
    return (mensaje.upper(), claveC)

def alfabetoSustitucion(clave):
    nuevaC = ''
    clave = clave.upper()
    abcd = list(letras)
    for i in range (len(clave)):
      if clave[i] not in nuevaC :
        nuevaC += clave[i]
        abcd.remove(clave[i])
    clave = nuevaC +''.join(abcd)
    return clave

def Mmatriz(clave):
  print('\nMatriz: ')
  for i in range (0,5):
    for j in range(5*i,5*(1+i)):
      print(clave[j],' ', end = ' ')
    print()
def cifrarM(claveC , mensaje):
    return cifrar_descifrar(claveC, mensaje , 'cifrar').upper()


def descifrarM(claveC, mensaje):
    return cifrar_descifrar(claveC, mensaje , 'descifrar').lower()

def cifrar_diagrama (a,b,claveC):
    return diagrama(a,b,claveC,'cifrar')
def descifrar_diagrama (a,b,claveC):
    return diagrama(a,b,claveC,'descifrar')
def diagrama (a, b, clave, modo):
    if modo == 'cifrar':
      if a==b: b ='X'
    else:
      if a==b:
        sys.exit()
    fila1,col1 = clave.index(a)//5 ,clave.index (a)%5
    fila2,col2 = clave.index(b)//5 ,clave.index (b)%5

    if modo == 'cifrar':
      pos = 1
    elif modo == 'descifrar':
      pos = -1
    if fila1 == fila2:
      return (clave[fila1*5+(col1+pos)%5] + clave[fila2*5+(col2+pos)%5])
    elif col1 == col2:
      return (clave[((fila1+pos)%5)*5+col1] + clave[((fila2+pos)%5)*5+col2])
    else:
      return (clave[fila1*5+col2]+ clave[fila2*5+col1])

def cifrar_descifrar(clave,  mensaje , modo):
    mensaje = re.sub('[^A-Z]','',mensaje.upper())
    mensaje = re.sub(r'[J]','I', mensaje)
    if len(mensaje) % 2 ==  1 :  mensaje += 'X'
    salida = ''
    for c in range(0,len(mensaje),2):
      salida += diagrama(mensaje[c], mensaje[c+1],clave,modo)
    return salida


if __name__ == "__main__":
    main()
