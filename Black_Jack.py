from random import choice, sample, shuffle                  #IMPORTACIONES

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

# defino estas variables para mostrar al usuario las cartas que hay y los valores que tiene cada carta

print('Las cartas con las que se juega son {},\n y los valores son {}'
      .format(cartas.keys(), cartas.values()))

                                                                                # DECLARACION DE VARIABLES

lista_cartas = list(cartas)             # creo una lista de cartas para despues dar dos cartas al usuario
shuffle(lista_cartas)


carta1 = choice(lista_cartas)
carta2 = choice(lista_cartas)                   # estas funciones se pueden cambiar por cartas_usuario = sample(lista_cartas)
valor1 = cartas [carta1]
valor2 = cartas [carta2]
suma_valor_cartas = valor1 + valor2 

carta_dealer1 = choice(lista_cartas)
carta_dealer2 = choice(lista_cartas)             # estas funciones se pueden cambiar por cartas_usuario = sample(lista_cartas)
valor1 = cartas [carta1]
valor_dealer1 = cartas [carta_dealer1]
valor_dealer2 = cartas [carta_dealer2]
suma_valores_dealer = valor_dealer1 + valor_dealer2

print(f'''Tus cartas son:                           
      {carta1} y {carta2} .
      y sus valores son: {valor1} y {valor2} . 
     En total suman {suma_valor_cartas} 
      ''')                                          # hago el print de las cartas del jugador, sus valores y la suma de los valores

print(f'''Las cartas del dealer son:
      {carta_dealer1} y {carta_dealer2}
      y sus valores son: {valor_dealer1} y {valor_dealer2}
      En total suman {suma_valores_dealer}
      ''')                                             # hago el print de las cartas del dealer, sus valores y la suma de los valores

if suma_valor_cartas <= suma_valores_dealer:
    print('Has perdido.') 
elif suma_valor_cartas >= suma_valores_dealer:
    print('Has ganado, ¡Enhorabuena!')
elif suma_valor_cartas == suma_valores_dealer:
    print('Habeis empatado. ')
