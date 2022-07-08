import re
import string

abcdario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 

def main():
    print("****************Cifrado vigenere***************")
    print("1. Cifrar")
    print("2. Descifrar")
    print("**********************************************")
    opcion = int(input('\n-Opcion -> '))
    
    if opcion == 1: #opcion cifrado
      cifrar()
    

    elif opcion == 2:#Opcion descifrado 
      Descifrar()

def divisionParametro(Texto, t):
    idx = 1
    salida = ''
    for char in Texto:
        if idx % t == 0:
            salida += char + " "
            idx += 1
        else:
            salida += char
            idx += 1

    return salida  
def cifrar():   

      text = input('-Mensaje -> ')
      Keyword = input('-Keyword -> ')
      t = int(input('-Parametro(t) -> '))
      salidaC = ""
      kpos = [] 
      for x in Keyword:
          kpos.append(abcdario.find(x))
      i = 0
      for x in text:
        if i == len(kpos):
            i = 0
        pos = abcdario.find(x) + kpos[i] 
        if pos > 25:
            pos = pos-26               
        salidaC += abcdario[pos].capitalize() 
        i +=1  
      print("\n***********************Mensaje encriptado***********************\n")
      print("Mensaje:",text)   
      print("El mensaje cifrado es -> :",divisionParametro(salidaC,t))

  
def Descifrar():
    entrada = input('-Mensaje -> ')
    text=entrada.replace(" ","")
    Keyword = input('-Keyword -> ')
    t = int(input('-Parametro(t) -> '))
    salidaD = ""
    kpos = []
    for x in Keyword:
        kpos.append(abcdario.find(x))
    i = 0
    for x in text:
      if i == len(kpos):
          i = 0
      pos = abcdario.find(x) - kpos[i]
      #print(pos)
      if pos < 0:
          pos = pos + 26
      salidaD += abcdario[pos]
      i +=1
    print("\n***********************Mensaje encriptado***********************\n")
    print("Mensaje:",text)   
    print("El mensaje cifrado es -> :",divisionParametro(salidaD,t))
if __name__ == "__main__":
    main()
