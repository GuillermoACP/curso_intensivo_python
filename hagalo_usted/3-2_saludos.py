'''
3-2. Saludos Usa la lista del ejercicio anterior, pero esta vez imprime un mensaje personalizado para cada persona. El texto puede ser el mismo, pero incluye el nombre de cada amigo.
'''

amigos = ['erick', 'arturo', 'fermin']

mensaje_erick = f'Hola {amigos[0].title()}, esto es Python\n'

mensaje_arturo = f'Hola {amigos[1].title()}, esto es Python\n'

mensaje_fermin = f'Hola {amigos[2].title()}, esto es Python\n'

print(mensaje_erick+mensaje_arturo+mensaje_fermin)