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