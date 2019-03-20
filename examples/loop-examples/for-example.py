arr_numbers = [10, 2, 4, [3, 7,13]]
#arr_numbers.sort()

#var_test = "Test"


for a in arr_numbers:
    print('Valor actual: {0}'.format(a))
    if isinstance(a, (int)):
        print("Es un numero")
    else:
        x=0
        while x < len(a):
            print(">> {0}".format(a[x]))
            x+=1
    
print("FIN!!!")
    

    # Celular: 83-32-55-48
    # lecona28@gmail.com
    # Subject: Nombre de Estudiante