def main():
    print("****************Cifrado Caesar***************")
    print("1. Cifrar")
    print("2. Descifrar")
    print("**********************************************")
    opcion = int(input('\n-Opcion -> '))
    
    if opcion == 1: #opcion cifrado
      cifrar()

    elif opcion == 2:#Opcion descifrado 
      Descifrar()

def cifrar():
  k = int(input('\n-Numero de permutacion (k) -> '))
  text = input('\n-Mensaje -> ')
  encriptado = ""
  for c in text:
      if c.isupper():
          c_unicode = ord(c)
          c_p = ord(c) - ord("A")
        # print(c_p)
          p= (c_p + k) % 26
        # print(p)
          codigo = p + ord("A")
          palabra = chr(codigo)
          encriptado = encriptado + palabra
      else:
          encriptado += c
  print("\n***********************Mensaje encriptado***********************")
  print("Mensaje:",text)
  print("Mensaje cifrado:",encriptado)

def Descifrar():
  k = int(input('\n-Numero de permutacion (k) -> '))
  text = input('\n-Mensaje -> ')
  des_encriptado = ""
  for c in text:
      if c.isupper():
          c_unicode = ord(c)
          c_p = ord(c) - ord("A")
        # print(c_p)
          p= (c_p - k) % 26
        # print(p)
          codigo = p + ord("A")
          palabra = chr(codigo)
          des_encriptado = des_encriptado + palabra
      else:
          des_encriptado += c

  print("\n***********************Mensaje des-encriptado***********************")
  print("Mensaje:",text)
  print("Mensaje desCifrado:",des_encriptado)
  return

if __name__ == "__main__":
    main()