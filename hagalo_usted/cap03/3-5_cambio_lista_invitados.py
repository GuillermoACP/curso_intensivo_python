'''
3-5. Cambios en la lista de invitados

Te acabas de enterar de que una de las personas que invitaste no podrá asistir. Debes enviar un nuevo conjunto de invitaciones.

Comienza con tu programa del ejercicio 3-4.

Añade una línea con print() al final del programa, indicando qué invitado no podrá asistir.

Modifica la lista y reemplaza a esa persona con una nueva.

Imprime un nuevo conjunto de mensajes de invitación.
'''

invitados = ['erick', 'arturo', 'fermin']


print(f'{invitados[0].title()}, estas invitado a mi boda')

print(f'{invitados[1].title()}, estas invitado a mi boda')

print(f'{invitados[2].title()}, estas invitado a mi boda')

no_asiste = 'erick'
invitados.remove(no_asiste)
print (f'{no_asiste.title()}, no podra asistir.\n')

invitados.append('alex')

print(f'{invitados[0].title()}, estas invitado a mi boda')

print(f'{invitados[1].title()}, estas invitado a mi boda')

print(f'{invitados[2].title()}, estas invitado a mi boda')