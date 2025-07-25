'''
-6. Más invitados

Has encontrado una mesa de comedor más grande, así que puedes invitar a más personas.

Comienza con tu programa del ejercicio 3-4 o 3-5.

Agrega una línea con print() al final, informando que has encontrado una mesa más grande.

Usa insert() para añadir un nuevo invitado al principio de la lista.

Usa insert() para añadir uno al medio.

Usa append() para añadir uno al final.

Imprime un nuevo conjunto de mensajes de invitación para todos.
'''
invitados = ['erick', 'arturo', 'fermin']


print(f'{invitados[0].title()}, estas invitado a mi boda')

print(f'{invitados[1].title()}, estas invitado a mi boda')

print(f'{invitados[2].title()}, estas invitado a mi boda')

no_asiste = 'erick'
invitados.remove(no_asiste)
print (f'\n{no_asiste.title()}, no podra asistir.\n')

invitados.append('alex')

print(f'{invitados[0].title()}, estas invitado a mi boda')

print(f'{invitados[1].title()}, estas invitado a mi boda')

print(f'{invitados[2].title()}, estas invitado a mi boda')

print(f'\nSe han encontrado mas mesas :D\n')

invitados.insert(0,'Gaby')
invitados.insert(2,'Maximo')
invitados.append('Gabriel')

print(f'{invitados[0].title()}, estas invitado a mi boda')

print(f'{invitados[1].title()}, estas invitado a mi boda')

print(f'{invitados[2].title()}, estas invitado a mi boda')

print(f'{invitados[3].title()}, estas invitado a mi boda')

print(f'{invitados[4].title()}, estas invitado a mi boda')