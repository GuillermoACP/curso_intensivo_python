'''
3-7. Lista de invitados cada vez más reducida

Te informan que la nueva mesa no llegará a tiempo. Solo puedes invitar a dos personas.

Comienza con tu programa del ejercicio 3-6.

Imprime un mensaje que indique que solo puedes invitar a dos personas.

Usa pop() para eliminar invitados uno por uno hasta que solo queden dos. Para cada persona eliminada, imprime un mensaje explicando que no podrá asistir.

Imprime un mensaje para cada una de las dos personas restantes, indicando que aún están invitadas.

Usa del para eliminar los últimos dos nombres de la lista.

Imprime la lista final para asegurarte de que esté vacía.


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

invitados.insert(0,'gaby')
invitados.insert(2,'maximo')
invitados.append('gabriel')

print(f'{invitados[0].title()}, estas invitado a mi boda')

print(f'{invitados[1].title()}, estas invitado a mi boda')

print(f'{invitados[2].title()}, estas invitado a mi boda')

print(f'{invitados[3].title()}, estas invitado a mi boda')

print(f'{invitados[4].title()}, estas invitado a mi boda')

print('\nSolo se podra invitar a 2 personas\n')

inv_pop1 = invitados.pop(1)
inv_pop2 = invitados.pop(2)
inv_pop3 = invitados.pop(3)
inv_pop4 = invitados.pop(0)
print(f'Lo siento {inv_pop1.title()}, no podras asistir.')
print(f'Lo siento {inv_pop2.title()}, no podras asistir.')
print(f'Lo siento {inv_pop3.title()}, no podras asistir.')
print(f'Lo siento {inv_pop4.title()}, no podras asistir.')

print(f'{invitados[0].title()},AUN estas invitado a mi boda')

print(f'{invitados[1].title()},AUN estas invitado a mi boda')

del invitados[0]
del invitados[0]
print(invitados)
