import numpy as np
def inputs():
   
    holes_positions = list()
    inp = dict()
    print("****************Turning Grill***************")
    temp =  int(input("\nOpcion:\n0. Encriptar\n1. Desencriptar\t"))
    inp["modo"] = temp
    temp = int(input("\nRotación:\n0. Horaria\n1. Antihoraria\t"))
    inp["direccion"] = temp
    temp = int(input("\nIngrese el tamaño:\t"))
    inp["tamaño"] = temp
    temp = int(input("\nIngrese la cantidad de hoyos:\t"))
    for i in range(temp):
        hole = np.array(input().strip().split()[:2], int)
        for j in hole:     
         holes_positions.append(hole)
    holes = np.zeros((inp["tamaño"], inp["tamaño"]), dtype=bool)
    for temp in holes_positions:
        holes[temp[0], temp[1]] = True
    inp["hl"] = holes
    temp = input("\nIngrese el mensaje:\t").replace(' ', '').upper()
    if inp["modo"] != 0:
        temp = temp + "-" * (inp["tamaño"] - len(temp))
        inp["matriz_m_c"] = np.array(list(temp)).reshape((inp["tamaño"], inp["tamaño"]))
    else:
        inp["mensaje_sin_c"] = temp
    return inp

def grill(inp):
    md = inp["modo"]
    inp["matriz_m_c"] = np.full((inp["tamaño"], inp["tamaño"]), '-') if md == 0 else inp["matriz_m_c"]
    result = ""
    k = 0
    dr = inp["direccion"]
    while k < 4:
        temp = np.rot90(inp["hl"], k, axes=((dr+1) % 2, (dr+0) % 2))
        for i in range(inp["tamaño"]):
            for j in range(inp["tamaño"]):
                if temp[i, j]:
                    if (md == 0) & (inp["matriz_m_c"][i, j] == "-"):
                        inp["matriz_m_c"][i, j] = inp["mensaje_sin_c"][0]
                        inp["mensaje_sin_c"] = inp["mensaje_sin_c"][1:]
                    elif (md != 0) & (inp["matriz_m_c"][i,j] != "-"):
                        result = result + inp["matriz_m_c"][i,j]
                        inp["matriz_m_c"][i,j] = "-"
        k = k + 1
    return ''.join([''.join(i)for i in inp["matriz_m_c"]]) if md == 0 else result

def main():
    inp = inputs()
    res = grill(inp)
    print("\nEl mensaje obtenido fue:\t", res)

if __name__ == "__main__":
    main()