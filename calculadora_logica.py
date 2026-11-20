import string

def inversor(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo):
    variable = variables_necesarias.index(proposicion[posicion + 1])
    nueva_columna = []
    for valor in variables_existentes[variable]:
        nueva_columna.append(not valor)

    variables_existentes.append(nueva_columna)
    variables_necesarias.append(simbolo)
    variables_finales.remove(proposicion[posicion + 1])
    proposicion[posicion:posicion + 2] = [simbolo]
    variables_finales.append(simbolo)
    return variables_existentes, proposicion, variables_necesarias, variables_finales

def Or(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo):
    if proposicion[posicion - 1] in variables_necesarias and proposicion[posicion + 1] in variables_necesarias:
        variable1 = variables_necesarias.index(proposicion[posicion - 1])
        variable2 = variables_necesarias.index(proposicion[posicion + 1])

        nueva_columna = []

        for i in range(len(variables_existentes[variable1])):
            nueva_columna.append(variables_existentes[variable1][i] or variables_existentes[variable2][i])

        variables_existentes.append(nueva_columna)
        variables_necesarias.append(simbolo)
        variables_finales.remove(proposicion[posicion - 1])
        variables_finales.remove(proposicion[posicion + 1])
        variables_finales.append(simbolo)

    return variables_existentes, variables_necesarias, variables_finales

def And(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo):
    if proposicion[posicion - 1] in variables_necesarias and proposicion[posicion + 1] in variables_necesarias:
        variable1 = variables_necesarias.index(proposicion[posicion - 1])
        variable2 = variables_necesarias.index(proposicion[posicion + 1])

        nueva_columna = []

        for i in range(len(variables_existentes[variable1])):
            nueva_columna.append(variables_existentes[variable1][i] and variables_existentes[variable2][i])

        variables_existentes.append(nueva_columna)
        variables_necesarias.append(simbolo)
        variables_finales.remove(proposicion[posicion - 1])
        variables_finales.remove(proposicion[posicion + 1])
        variables_finales.append(simbolo)

    return variables_existentes, variables_necesarias, variables_finales

def implicacion(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo):
    if proposicion[posicion - 1] in variables_necesarias and proposicion[posicion + 1] in variables_necesarias:
        variable1 = variables_necesarias.index(proposicion[posicion - 1])
        variable2 = variables_necesarias.index(proposicion[posicion + 1])

        nueva_columna = []

        for i in range(len(variables_existentes[variable1])):
            nueva_columna.append(not variables_existentes[variable1][i] or variables_existentes[variable2][i])

        variables_existentes.append(nueva_columna)
        variables_necesarias.append(simbolo)
        variables_finales.remove(proposicion[posicion - 1])
        variables_finales.remove(proposicion[posicion + 1])
        variables_finales.append(simbolo)

    return variables_existentes, variables_necesarias, variables_finales

def bicondicional(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo):
    if proposicion[posicion - 1] in variables_necesarias and proposicion[posicion + 1] in variables_necesarias:
        variable1 = variables_necesarias.index(proposicion[posicion - 1])
        variable2 = variables_necesarias.index(proposicion[posicion + 1])

        nueva_columna = []

        for i in range(len(variables_existentes[variable1])):
            nueva_columna.append((variables_existentes[variable1][i] and variables_existentes[variable2][i]) or (not variables_existentes[variable1][i] and not variables_existentes[variable2][i]))

        variables_existentes.append(nueva_columna)
        variables_necesarias.append(simbolo)
        variables_finales.remove(proposicion[posicion - 1])
        variables_finales.remove(proposicion[posicion + 1])
        variables_finales.append(simbolo)


    return variables_existentes, variables_necesarias, variables_finales

def buscar_parentesis(proposicion):
    pila = []

    for i, token in enumerate(proposicion):
        if token == "(":
            pila.append(i)

        elif token == ")":
            a = pila.pop()
            b = i
            return a, b

    return None

def nuevo_simbolo(proposicion, variables_necesarias):
    usados = set(proposicion) | set(variables_necesarias)

    for letra in string.ascii_lowercase:
        if letra not in usados:
            return letra

def imprimir_columnas(variables_existentes, variables_necesarias, variables_finales, variables_originales):
    impresos = []
    for variable in variables_finales:
        if variable not in variables_originales and variable not in impresos:
            posicion = variables_necesarias.index(variable)
            print(f"{variable}: {variables_existentes[posicion]}")
            impresos.append(variable)

def operacion():
    print("Operaciones disponibles: '^' - and (y), 'V' - or (o), '→' - (implicación), '↔' - (bidireccional)\n")
    print()
    while True:
        proposicion = input("Ingrese su operacion: ")

        variables = [proposicion.count("p"), proposicion.count("q"), proposicion.count("r"), proposicion.count("s")]
        variables_necesarias = sum(variables)

        if proposicion == "!p":
            print("""===Tabla de Verdad===
Falso
Falso
Verdadero
Verdadero""")
            break
        elif "^" not in proposicion and "∧" not in proposicion and "V" not in proposicion and "→" not in proposicion and "↔" not in proposicion:
            print("Variable/s invalida/s o muy pocas variables compuestas")
            continue
        elif variables_necesarias <= 1:
            print("Operacion invalida")
            continue
        elif proposicion[0] != "p":
            contador = 0
            for variable in proposicion:
                if variable == "q" or variable == "r" or variable == "s" or variable == ")":
                    contador+=1
                    continue
                elif variable == "p" and contador == 0:
                    break
            else:
                print("Debe ingresar 'p' como valor inicial.")
                continue
            break
        break
    return proposicion

proposicion = operacion()
proposicion = proposicion.replace("^", "∧")
proposicion = list(proposicion)

while True:
    variables_existentes = []
    variables_necesarias = []
    n=0
    if "p" in proposicion:
        n+=1
        variables_necesarias.append("p")
    if "q" in proposicion:
        n+=1
        variables_necesarias.append("q")
    if "r" in proposicion:
        n+=1
        variables_necesarias.append("r")
    if "s" in proposicion:
        n+=1
        variables_necesarias.append("s")

    n=2**n

    for variables in variables_necesarias:
        if  variables == "p":
            p = []
            for _ in range(n // 2):
                p.append(True)
            for _ in range(n // 2):
                p.append(False)
            variables_existentes.append(p)
        elif variables == "q":
            q = []
            a = 2 ** variables_necesarias.index("q")
            b=2**(len(variables_necesarias) - variables_necesarias.index("q") - 1)
            for _ in range(a):
                for _ in range(b):
                    q.append(True)
                for _ in range(b):
                    q.append(False)
            variables_existentes.append(q)
        elif variables == "r":
            r = []
            a = 2 ** variables_necesarias.index("r")
            b = 2 ** (len(variables_necesarias) - variables_necesarias.index("r") - 1)
            for _ in range(a):
                for _ in range(b):
                    r.append(True)
                for _ in range(b):
                    r.append(False)
            variables_existentes.append(r)
        elif variables == "s":
            s = []
            a = 2 ** variables_necesarias.index("s")
            b = 2 ** (len(variables_necesarias) - variables_necesarias.index("s") - 1)
            for _ in range(a):
                for _ in range(b):
                    s.append(True)
                for _ in range(b):
                    s.append(False)
            variables_existentes.append(s)
    break

print()
impresion = "PROCESO DE RESOLUCION"
print(impresion.center(50, "="))
print(" ".join(proposicion))
print()
print(variables_existentes)
print()

variables_originales = variables_necesarias.copy()
variables_finales = [token for token in proposicion if token in variables_necesarias]

def reconocimiento_de_operaciones(proposicion, variables_necesarias, variables_existentes, variables_finales):

    while len(proposicion) > 1:

        imprimir = False
        resultado = buscar_parentesis(proposicion)

        if resultado is None:
            inicio = 0
            fin = len(proposicion)
            a = None
        else:
            a, b = resultado
            inicio = a + 1
            fin = b

        operador = None

        for candidato in ["∧", "V", "→", "↔"]:
            if candidato in proposicion[inicio:fin]:
                operador = candidato
                break

        posicion = None

        for i in range(len(proposicion) - 1):
            if proposicion[i] == "!" and proposicion[i + 1] in variables_necesarias:
                posicion = i
                break

        if posicion is not None:
            simbolo = nuevo_simbolo(proposicion, variables_necesarias)
            variables_existentes, proposicion, variables_necesarias, variables_finales = inversor(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo)
            print(" ".join(proposicion))
            print()
            imprimir_columnas(variables_existentes, variables_necesarias, variables_finales, variables_originales)
            print()
            continue

        if resultado is not None:
            if fin - inicio == 1:
                proposicion.pop(b)
                proposicion.pop(a)
                continue

        if operador is not None:
            posicion = proposicion.index(operador, inicio, fin)
            simbolo = nuevo_simbolo(proposicion, variables_necesarias)

            if operador == "∧":
                variables_existentes, variables_necesarias, variables_finales = And(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo)

            elif operador == "V":
                variables_existentes, variables_necesarias, variables_finales = Or(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo)

            elif operador == "→":
                variables_existentes, variables_necesarias, variables_finales = implicacion(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo)

            elif operador == "↔":
                variables_existentes, variables_necesarias, variables_finales = bicondicional(variables_existentes, proposicion, variables_necesarias, variables_finales, posicion, simbolo)

            proposicion[posicion - 1:posicion + 2] = [simbolo]

            print(" ".join(proposicion))
            print()
            imprimir_columnas(variables_existentes, variables_necesarias, variables_finales, variables_originales)
            print()

        elif "!" in proposicion and "(" in proposicion and ")" in proposicion:
            proposicion.pop(proposicion.index("!") + 1)
            proposicion.pop(proposicion.index(")", proposicion.index("!") + 1))

    return variables_existentes, proposicion, variables_necesarias

variables_existentes, proposicion, variables_necesarias = reconocimiento_de_operaciones(proposicion, variables_necesarias, variables_existentes, variables_finales)

resultado_final = proposicion[0]
encabezados = variables_originales + [resultado_final]

print()
impresion = "TABLA DE VERDAD"
print(impresion.center(50, "="))
print(" | ".join(encabezados))

for i in range(len(variables_existentes[0])):
    fila = []
    for variable in encabezados:
        posicion = variables_necesarias.index(variable)
        if variables_existentes[posicion][i]:
            fila.append("V")
        else:
            fila.append("F")
    print(" | ".join(fila))

print()
input("Presiona enter para salir.")
