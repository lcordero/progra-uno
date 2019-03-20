
# Definir funcion
def dividir(dividendo, divisor):
    try:
        print dividendo, '/', divisor, '=', dividendo/divisor
    except Exception, Argument:
        print 'ERROR:', Argument
    return

# Llamar funcion
dividir(10,5)