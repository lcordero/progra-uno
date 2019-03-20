def suma(number1, number2):
    return number1 + number2

def resta(number1, number2):
    return number1 - number2

def divide(number1, number2):
    return number1 / number2

def multiplica(number1, number2):
    return number1 * number2

def doMath(number1, number2, operator):
    # Define diccionario
    math_functions = {
        "+": suma,
        "-": resta,
        "/": divide,
        "*": multiplica
    }

    # Llamar funcion
    math_func = math_functions.get(operator)
    return math_func(number1, number2)

# Solicitar informacion
def requestInfo():
    val1=int(input("Val #1:"))
    val2=int(input("Val #2:"))
    oper=str(raw_input("Operador:")) # <<-- esto xq es un simbolo
    return doMath(val1, val2, oper)

print(requestInfo())