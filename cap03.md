# PRESENTACIÓN DE LAS LISTAS

En este capítulo y el siguiente, aprenderás qué son las listas y cómo empezar a trabajar con sus elementos.
Las listas te permiten almacenar conjuntos de información en un solo lugar, ya sea que contengan solo unos pocos elementos o millones. Son una de las características más poderosas de Python, fácilmente accesibles para programadores principiantes, y reúnen muchos conceptos clave de la programación.

## ¿Qué es una lista?

Una lista es una colección de elementos ordenados. Puedes crear una lista con las letras del alfabeto, los dígitos del 0 al 9 o los nombres de todos los miembros de tu familia. Puedes incluir lo que desees en una lista, y los elementos no tienen que estar relacionados entre sí.

Como una lista normalmente contiene más de un elemento, es buena práctica darle un nombre en plural, como letras, numeros o nombres.

En Python, los corchetes `([])` indican una lista, y los elementos se separan con comas. Aquí tienes un ejemplo de una lista que contiene algunos tipos de bicicletas:

```python
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)
```

Si le pides a Python que imprima esta lista, te devolverá su representación completa, incluyendo los corchetes:

```shell
['trek', 'cannondale', 'redline', 'specialized']
```

Dado que esto no es lo ideal para mostrar a los usuarios, veamos cómo acceder a elementos individuales.

### Acceder a elementos en una lista

Las listas están ordenadas, así que puedes acceder a cualquier elemento indicando su posición (índice). Para hacerlo, escribe el nombre de la lista seguido del índice entre corchetes:

```python
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas[0])
```

Este código devuelve solo el primer elemento de la lista, sin corchetes:

```
trek
```

Este es el tipo de resultado limpio que deseas mostrar a los usuarios.

También puedes usar los métodos de cadena del capítulo anterior en los elementos de una lista. Por ejemplo, puedes formatear el primer elemento usando `.title()`:

```python
print(bicicletas[0].title())
```

Esto mostrará:
```
Trek
```
### Los índices comienzan en 0

Python considera que el primer elemento de una lista está en la posición 0, no en la 1. Esto es común en muchos lenguajes de programación, por razones relacionadas con cómo funcionan las estructuras de datos internamente.

Por ejemplo, para acceder al cuarto elemento de una lista, deberás usar el índice 3:
```python
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas[1])
print(bicicletas[3])
```
Este código devuelve el segundo y el cuarto elementos:
```
cannondale
specialized
```
### Acceder al último elemento de una lista

Python tiene una sintaxis especial para acceder al último elemento: simplemente usa el índice -1.
```python
print(bicicletas[-1])
```
Esto devuelve:
```
specialized
```
Esto es útil cuando no conoces exactamente el tamaño de la lista. También puedes usar índices negativos para acceder a otros elementos desde el final:

    -2 es el penúltimo,

    -3 es el antepenúltimo, y así sucesivamente.

### Usar valores individuales de una lista

Puedes usar los valores individuales de una lista como lo harías con cualquier otra variable. Por ejemplo, puedes construir un mensaje con una cadena `f-string`:
```python
bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
mensaje = f"Mi primera bicicleta fue una {bicicletas[0].title()}."
print(mensaje)
```
Este código mostrará:
```
Mi primera bicicleta fue una Trek.
```
---
### INTÉNTALO TÚ MISMO

Prueba los siguientes ejercicios para practicar el uso de listas en Python. Te recomiendo crear una nueva carpeta para los ejercicios de cada capítulo, así los mantendrás organizados.

3-1. Nombres
Guarda los nombres de algunos de tus amigos en una lista llamada nombres. Imprime el nombre de cada persona accediendo a los elementos uno por uno.

3-2. Saludos
Usa la lista del ejercicio anterior, pero esta vez imprime un mensaje personalizado para cada persona. El texto puede ser el mismo, pero incluye el nombre de cada amigo.

3-3. Tu propia lista
Piensa en un medio de transporte que te guste, como una motocicleta o un automóvil. Crea una lista con varios ejemplos. Usa la lista para imprimir mensajes como:
"Me gustaría tener una motocicleta Honda."

---

## Modificar, agregar y eliminar elementos

La mayoría de las listas que crearás serán dinámicas, lo que significa que las construirás al inicio del programa y luego irás agregando o eliminando elementos a medida que el programa se ejecute.

Por ejemplo, podrías crear un juego donde un jugador dispare a extraterrestres que aparecen en el cielo. Almacenarías a los alienígenas activos en una lista y, cada vez que uno sea eliminado, lo quitarías de esa lista. Cuando aparece uno nuevo en pantalla, lo agregarías. Así, la lista de alienígenas crecerá o disminuirá dinámicamente durante el juego.

### Modificar elementos de una lista

Modificar un elemento en una lista es tan simple como acceder a él mediante su índice y luego asignarle un nuevo valor. La sintaxis es similar a la de acceso:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

motocicletas[0] = 'ducati'
print(motocicletas)
```

Primero definimos la lista motocicletas con 'honda' como primer elemento. Luego lo reemplazamos por 'ducati'. El resultado será:

```shell
['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']
```
Puedes modificar cualquier elemento de una lista, no solo el primero.

### Agregar elementos a una lista

Agregar nuevos elementos a una lista es una operación muy común. Puedes necesitarlo para añadir jugadores, objetos, usuarios, mensajes, etc. Python proporciona varias formas de hacerlo.
### Agregar al final de la lista con `append()`

La forma más simple es usar el método `.append()` para añadir un elemento al final:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)

motocicletas.append('ducati')
print(motocicletas)
```
Esto produce:

```shell
['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']
```

También puedes construir una lista desde cero:

```python
motocicletas = []
motocicletas.append('honda')
motocicletas.append('yamaha')
motocicletas.append('suzuki')
print(motocicletas)
```

Resultado:

```shell
['honda', 'yamaha', 'suzuki']
```

Este enfoque es útil cuando no conoces los datos de antemano. Puedes comenzar con una lista vacía y agregar elementos conforme se necesiten.

### Insertar elementos en una posición específica

Usa `.insert(posición, valor)` para insertar un elemento en cualquier parte de la lista:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
motocicletas.insert(0, 'ducati')
print(motocicletas)
```

Resultado:
```shell
['ducati', 'honda', 'yamaha', 'suzuki']
```

El método `insert()` mueve los demás elementos hacia la derecha.

### Eliminar elementos de una lista

Puedes eliminar elementos de una lista según su posición o su valor.
Usar `del` para eliminar por índice

Si conoces la posición del elemento:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
del motocicletas[0]
print(motocicletas)
```

Resultado:
```shell
['yamaha', 'suzuki']
```

También puedes eliminar otro elemento:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
del motocicletas[1]
print(motocicletas)
```

Resultado:

```shell
['honda', 'suzuki']
```
Ten en cuenta que no puedes volver a acceder al valor eliminado después de usar `del`.
### Usar `pop()` para eliminar y usar un valor

Si deseas usar el valor eliminado, usa `.pop()`. Este método elimina el último elemento de la lista y te permite almacenarlo:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motocicletas.pop()

print(motocicletas)
print(popped_motorcycle)
```

Salida:

```shell
['honda', 'yamaha']
suzuki
```

Esto es útil cuando necesitas trabajar con el elemento que estás quitando. Por ejemplo:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
ultima_moto = motocicletas.pop()
print(f"La última motocicleta que tuve fue una {ultima_moto.title()}.")
```
Resultado:

```shell
La última motocicleta que tuve fue una Suzuki.
```
### Usar pop() con un índice

También puedes usar `pop()` para quitar un elemento específico:

```python
motocicletas = ['honda', 'yamaha', 'suzuki']
primera_moto = motocicletas.pop(0)
print(f"La primera motocicleta que tuve fue una {primera_moto.title()}.")
```

Resultado:
```shell
La primera motocicleta que tuve fue una Honda.
```
¿Cuándo usar `del` y cuándo usar `pop()`?

    Usa **del** cuando no necesites el valor que estás eliminando.

    Usa **pop()** si quieres guardar o usar el valor eliminado.

Eliminar un elemento por valor

A veces no conocerás la posición del elemento que deseas eliminar de una lista. Si solo conoces el valor del elemento, puedes usar el método `remove()` para eliminarlo.

Por ejemplo, supongamos que queremos eliminar el valor `'ducati'` de la lista de motocicletas:

```python
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocicletas)
motocicletas.remove('ducati')
print(motocicletas)
```

Aquí, el método `remove()` le indica a Python que busque en la lista el valor 'ducati' y lo elimine. El resultado sería:

```shell
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']
```

También puedes usar `remove()` para trabajar con un valor que necesitas eliminar, pero que deseas conservar en una variable antes de borrarlo. Por ejemplo:

```python
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocicletas)

demasiado_cara = 'ducati'
motocicletas.remove(demasiado_cara)
print(motocicletas)

print(f"\nUna {demasiado_cara.title()} es demasiado cara para mí.")
```
Este código produce:

```shell
['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

Una Ducati es demasiado cara para mí.
```

    Nota: el método remove() solo elimina la primera aparición del valor especificado. Si el valor aparece varias veces en la lista, necesitarás usar un bucle para eliminar todas las apariciones. Verás cómo hacerlo en el Capítulo 7.

---
### INTÉNTALO TÚ MISMO

Los siguientes ejercicios son un poco más complejos que los del Capítulo 2, pero te dan la oportunidad de practicar todas las formas en que se pueden usar listas:

3-4. Lista de invitados

Si pudieras invitar a cenar a cualquier persona, viva o fallecida, ¿a quién invitarías?

Haz una lista con al menos tres personas a las que te gustaría invitar a cenar.

Luego, usa la lista para imprimir un mensaje de invitación personalizado para cada persona.

3-5. Cambios en la lista de invitados

Te acabas de enterar de que una de las personas que invitaste no podrá asistir.
Debes enviar un nuevo conjunto de invitaciones.

Comienza con tu programa del ejercicio 3-4.

Añade una línea con print() al final del programa, indicando qué invitado no podrá asistir.

Modifica la lista y reemplaza a esa persona con una nueva.

Imprime un nuevo conjunto de mensajes de invitación.

3-6. Más invitados

Has encontrado una mesa de comedor más grande, así que puedes invitar a más personas.

Comienza con tu programa del ejercicio 3-4 o 3-5.

Agrega una línea con print() al final, informando que has encontrado una mesa más grande.

Usa insert() para añadir un nuevo invitado al principio de la lista.

Usa insert() para añadir uno al medio.

Usa append() para añadir uno al final.

Imprime un nuevo conjunto de mensajes de invitación para todos.

3-7. Lista de invitados cada vez más reducida

Te informan que la nueva mesa no llegará a tiempo. Solo puedes invitar a dos personas.

Comienza con tu programa del ejercicio 3-6.

Imprime un mensaje que indique que solo puedes invitar a dos personas.

Usa pop() para eliminar invitados uno por uno hasta que solo queden dos.
Para cada persona eliminada, imprime un mensaje explicando que no podrá asistir.

Imprime un mensaje para cada una de las dos personas restantes, indicando que aún están invitadas.

Usa del para eliminar los últimos dos nombres de la lista.

Imprime la lista final para asegurarte de que esté vacía.

---

## Organizar una lista

Muchas veces, las listas se crean en un orden aleatorio o impredecible. Aunque no siempre puedes controlar ese orden, muchas veces querrás presentar la información en un orden específico.

Python ofrece varias formas de ordenar listas, según tus necesidades:
Ordenar una lista permanentemente con `sort()`

El método `sort()` ordena una lista de forma permanente.
Por ejemplo, si tienes una lista de automóviles y deseas ordenarlos alfabéticamente:

```python
autos = ['bmw', 'audi', 'toyota', 'subaru']
autos.sort()
print(autos)
```

Esto muestra:

```shell
['audi', 'bmw', 'subaru', 'toyota']
```

También puedes ordenarla en orden alfabético inverso con `reverse=True`:

```python
autos = ['bmw', 'audi', 'toyota', 'subaru']
autos.sort(reverse=True)
print(autos)
```

Resultado:

```shell
['toyota', 'subaru', 'bmw', 'audi']
```
Ordenar una lista temporalmente con `sorted()`

Si no quieres modificar el orden original de la lista, puedes usar la función sorted():

```python
autos = ['bmw', 'audi', 'toyota', 'subaru']

print("Lista original:")
print(autos)

print("\nLista ordenada:")
print(sorted(autos))

print("\nLista original nuevamente:")
print(autos)
```

Resultado:

```shell
Lista original:
['bmw', 'audi', 'toyota', 'subaru']

Lista ordenada:
['audi', 'bmw', 'subaru', 'toyota']

Lista original nuevamente:
['bmw', 'audi', 'toyota', 'subaru']
```
Puedes usar `sorted(autos, reverse=True)` para mostrarla ordenada alfabéticamente en sentido inverso sin modificar la lista original.

    Nota: ordenar listas con mayúsculas y minúsculas puede ser más complejo. Este libro no abordará eso en detalle por ahora.

### Imprimir una lista en orden inverso

Si deseas invertir el orden de una lista (sin orden alfabético), puedes usar `reverse()`:

```python
autos = ['bmw', 'audi', 'toyota', 'subaru']
autos.reverse()
print(autos)
```
Esto muestra:

```shell
['subaru', 'toyota', 'audi', 'bmw']
```

Llamar a `reverse()` dos veces restaura el orden original.

### Encontrar la longitud de una lista

Para saber cuánt elementos hay en una lista, usa la función `len()`:

```python
autos = ['bmw', 'audi', 'toyota', 'subaru']
print(len(autos))
```
Resultado:

```
4
```
    Nota: Python cuenta los elementos desde 1 al usar len(), pero los índices comienzan desde 0.

---
### INTÉNTALO TÚ MISMO
3-8. Ver el mundo

Piensa en al menos cinco lugares del mundo que te gustaría visitar.

- Guarda esas ubicaciones en una lista (que no esté ordenada alfabéticamente).

- Imprime la lista en su orden original.

- Usa sorted() para mostrar la lista en orden alfabético sin modificarla.

- Muestra que la lista sigue en su orden original.

- Usa sorted() con reverse=True para mostrar la lista en orden alfabético inverso.

- Vuelve a mostrar la lista para comprobar que no cambió.

- Usa reverse() para invertir el orden original.

- Usa reverse() otra vez para restaurarlo.

- Usa sort() para ordenar la lista permanentemente.

    
- Usa sort(reverse=True) para ordenarla de forma permanente en orden inverso.

3-9. Invitados a cenar

Con uno de los programas anteriores (ejercicio 3-4 a 3-7), usa len() para mostrar cuántas personas están invitadas a cenar.

3-10. Cada función

Piensa en una categoría de cosas que podrías almacenar en una lista (montañas, ríos, países, etc.).
Escribe un programa que cree una lista con esos elementos y utiliza cada función que se presentó en este capítulo al menos una vez.

---
### Evitar errores de índice al trabajar con listas

Hay un tipo de error que es muy común cuando trabajas con listas por primera vez.
Supongamos que tienes una lista con tres elementos y tratas de acceder al cuarto:
```python
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas[3])
```
Este ejemplo produce un error de índice:
```shell
Traceback (most recent call last):
  File "motocicletas.py", line 2, in <module>
    print(motocicletas[3])
IndexError: list index out of range
```
Python intenta darte el elemento con índice 3, pero al revisar la lista no encuentra ningún elemento en esa posición.
Esto ocurre porque la indexación en las listas comienza en 0, no en 1.
Es común pensar que el “tercer” elemento está en el índice 3, pero en realidad está en el índice 2:

    Primer elemento → índice 0

    Segundo elemento → índice 1

    Tercer elemento → índice 2

Un IndexError significa que Python no pudo encontrar un elemento en la posición que pediste.
Si te ocurre este error, prueba restar 1 al índice y ejecuta de nuevo el programa para ver si se soluciona.
Acceder al último elemento de una lista con -1

Cuando quieras acceder al último elemento de una lista, puedes usar el índice -1.
Esto siempre funcionará, incluso si el tamaño de la lista ha cambiado desde la última vez:

motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas[-1])

Este código imprimirá:

suzuki

Sin embargo, este enfoque provocará un error si la lista está vacía:

motocicletas = []
print(motocicletas[-1])

Python no puede devolver un elemento inexistente, así que lanzará otro error de índice:

Traceback (most recent call last):
  File "motocicletas.py", line 3, in <module>
    print(motocicletas[-1])
IndexError: list index out of range

Cómo depurar errores de índice

Si te ocurre un error de índice y no estás seguro de por qué, intenta imprimir la lista completa o usar len() para ver cuántos elementos tiene.
A veces la lista no es como esperabas, especialmente si el programa la ha modificado dinámicamente.

Ver el contenido real de la lista, o su longitud exacta, puede ayudarte a detectar el problema.
INTÉNTALO TÚ MISMO
3-11. Error intencional

Si aún no has obtenido un IndexError en tus programas, intenta provocarlo.
Modifica uno de tus programas para acceder a un índice fuera del rango de la lista.
Luego corrige el error antes de cerrar el programa.
Resumen

En este capítulo aprendiste:

    Qué son las listas y cómo trabajar con sus elementos.

    Cómo definir, agregar y eliminar elementos.

    Cómo ordenarlas de manera permanente y temporal.

    Cómo encontrar la longitud de una lista con len().

    Cómo evitar errores de índice al trabajar con posiciones inexistentes.

En el Capítulo 4, aprenderás a trabajar con los elementos de una lista de forma más eficiente.
Aprenderás a recorrer cada elemento con solo unas pocas líneas de código, lo cual te permitirá trabajar incluso con listas que tengan miles o millones de elementos.