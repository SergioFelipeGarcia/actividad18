#ejercicio3
#entrada
print(' son 20 preguntas dime las acertadas,las incorrectas y las sin contestar')

acertadas=int(input('preguntas acertadas: '))
incorrectas=int(input('preguntas incorrectas: '))
sinresponder=int(input('preguntas sin responder: '))

#Proceso

resultado=((acertadas*0.5)-(incorrectas*0.25)+(sinresponder*0))

#Salida
print(resultado)



