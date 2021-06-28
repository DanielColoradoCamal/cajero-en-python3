from datetime import datetime

dt = datetime.now()    # Fecha y hora actual


# Definicion de Montos de las cuentas
Monto_1 = 50000  # Cuenta de Ahoroo
Monto_2 = 15000  # Cuenta de Nomina
Monto_3 = 5500  # Tarjeta de Credito




while 1 == 1:  # Ciclo infinito, para el funcionamiento continuo del cajero

    # Pantalla de bienvenida

    print ('CAJERO AUTOMATICO')
    j = input('Presione ENTRAR para comenzar')
    if j == (''):
        print ('Digite su clave')

    # Definicion de variables importantes dentro de los ciclos y de la clave de usuario

    m = 0

    clave = 2020

    conterr = 2

    cont = 2

    c_ingresada = int(input(""))

    while (cont >= 1):  # Ingreso de clave

        if c_ingresada == clave:
            m = 1
            cont = cont = 0

        elif c_ingresada != clave:
            print('Clave erronea. Intentos restantes:', conterr)
            cont = cont - 1
            c_ingresad = c_ingresada = int(input(""))
            conterr = conterr - 1

            if cont == 0 and clave != c_ingresada:
                print('Clave incorrecta. Exedio el numero de veces permitidas')
                print ('')
                print ('')
                print ('')
                print ('')


            if cont == 0 and clave == c_ingresada:
                m = 1

    #############################################################################

    if m == 1:  # Si la clave es ingresada con exito Inprimira Bienvenido y comenzara el uso del cajero
        print ('Bienvenido')

        Operacion = 1  # Definimos operacion en 1 para que comience el funcionamiento
        while Operacion == 1:  # Comienzo de las operaciones del cajero

            if Monto_1 < 0:  # Advertencia en caso de que haya una deuda
                print ('Usted debe un total de', Monto_1 * (-1), 'En la Cuenta de Ahorro ')
            if Monto_2 < 0:
                print ('Usted debe un total de', Monto_2 * (-1), 'En la Cuenta de Nomina ')
            if Monto_3 < 0:
                print ('Usted debe un total de', Monto_3 * (-1), 'En la Tarjeta de Credito ')

            # Seleccion de operacion

            print ('Seleccione la operacion a realizar')
            print (1, '    ', 'Consulta de saldo')
            print (2, '    ', 'Retiro de dinero')
            print (3, '    ', 'Deposito de dinero')
       

            Operacion = Operacion = int(input("Elije una operacion: "))

            # Seleccion de Cuenta

            print ('Estas son las cuentas a su nombre, porfavor seleccione una de ellas')
            print (1, '    ', 'Cuenta de Ahorro')
            print (2, '    ', 'Cuenta de Nomina')
            print (3, '    ', 'Tarjeta de Credito')
            Cuenta = int(input("Seleccione su cuenta: "))

            #############################################################################

            # Consulta de Saldo

            if Operacion == 1:  # Si la operacion es consulta de saldo

                if Cuenta == 1:
                    print ('Saldo disponible:  ', '$', Monto_1)
                elif Cuenta == 2:
                    print ('Saldo disponible:  ', '$', Monto_2)
                elif Cuenta == 3:
                    print ('Saldo disponible:  ', '$', Monto_3) ,

            #############################################################################

            # Retiro de dinero

            if Operacion == 2:  # Si la operacion es Retiro

                print ('Seleccione el Monto a Retirar')

                Monto = int(input(''))

                if Cuenta == 1:

                    if Monto <= 5001 :


                        if Monto <= Monto_1:

                            if Monto <= Monto_1:
                                Monto_1 = Monto_1 - Monto
                                print ('Su nuevo monto es: ', '$', Monto_1)
                            else:
                                    print ('Saldo insuficiente')
                    elif Monto > 5001 :

                        print ('El Monto maximo es $ 5000')
                    else:
                            print('Saldo insuficiente')



                if Cuenta == 2:

                    print ('Seleccione el Monto a Retirar')

                    Monto = int(input(''))

                    if Monto <= 5001 :


                        if Monto <= Monto_2:

                            if Monto <= Monto_2:
                                Monto_2 = Monto_2 - Monto
                                print ('Su nuevo monto es: ', '$', Monto_2)
                            else:
                                    print ('Saldo insuficiente')
                    elif Monto > 5001 :

                        print ('El Monto maximo es $ 5000')
                    else:
                            print('Saldo insuficiente')


                if Cuenta == 3:

                    print ('Seleccione el Monto a Retirar')

                    Monto = int(input(''))

                    if Monto <= 5000 :


                        if Monto <= Monto_3:

                            if Monto <= Monto_3:
                                Monto_3 = Monto_3 - Monto
                                print ('Su nuevo monto es: ', '$', Monto_3)
                            else:
                                    print ('Saldo insuficiente')
                    elif Monto > 5001 :

                        print ('El Monto maximo es $ 5000')
                    else:
                            print('Saldo insuficiente')
            #############################################################################

            # Deposito de dinero

            if Operacion == 3:  # Si la operacion es deposito

                Monto_Ingresado = int(input('Monto Ingresado:            '))  # Ingresamos el monto a depositar
                if Cuenta == 1:

                    Monto_1 = Monto_1 + Monto_Ingresado
                    print ('Su nuevo monto es: ', '$', Monto_1)
                elif Cuenta == 2:

                    Monto_2 = Monto_2 + Monto_Ingresado
                    print ('Su nuevo monto es: ', '$', Monto_2)
                elif Cuenta == 3:

                    Monto_3 = Monto_3 + Monto_Ingresado
                    print ('Su nuevo monto es: ', '$', Monto_3)

    
            #############################################################################

            # Pregunta si desea otra operacion

            print ('Alguna otra operacion?')
            print (1, '    ', 'Si')
            print (2, '    ', 'No')
            Operacion = Operacion = int(input(''))  # Responde a la interrogante anterior
            # Si la respuesta es si, vuelve a preguntar la operacion
            # Sin cerrar la sesion

            if Operacion == 2:  # Si no es asi finaliza la sesion
                print ('SESION FINALIZADA')
                print ('')
                print ('')
                print ('')
                print ('')

input()