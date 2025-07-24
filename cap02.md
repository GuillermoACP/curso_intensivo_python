# VARIABLES Y TIPOS DE DATOS SIMPLES

En este capítulo aprenderás sobre los diferentes tipos de datos con los que puedes trabajar en tus programas de Python. También aprenderás a utilizar variables para representar datos en tus programas.

## ¿Qué sucede realmente cuando ejecutas `hello_world.py`?

Echemos un vistazo más detallado a lo que hace Python cuando ejecuta `hello_world.py`. Resulta que Python realiza bastante trabajo, incluso al ejecutar un programa muy simple:

```python
# hello_world.py
print("¡Hola mundo Python!")
```
Cuando ejecutas este código, deberías ver el siguiente resultado:
```
¡Hola mundo Python!
```
Al ejecutar el archivo `hello_world.py`, la extensión .py indica que se trata de un programa de Python. Luego, tu editor ejecuta el archivo a través del intérprete de Python, que lee el programa y determina el significado de cada palabra. Por ejemplo, cuando el intérprete encuentra la palabra `print` seguida de paréntesis, muestra en pantalla el contenido que se encuentra dentro de ellos.

Mientras escribes tus programas, tu editor resalta diferentes partes del código de distintas formas. Por ejemplo, reconoce que `print()` es el nombre de una función y lo muestra en un color, mientras que muestra `"¡Hola mundo Python!"` en otro color porque no es código Python. Esta característica se llama resaltado de sintaxis y es muy útil cuando estás empezando a escribir tus propios programas.
Variables

Intentemos usar una variable en `hello_world.py`. Agrega una nueva línea al inicio del archivo y modifica la segunda línea de la siguiente manera:
```python
# hello_world.py
mensaje = "¡Hola mundo Python!"
print(mensaje)
```
Ejecuta el programa para ver qué sucede. Deberías obtener el mismo resultado que antes:
```
¡Hola mundo Python!
```
Hemos añadido una variable llamada mensaje. Cada variable está asociada a un valor, que es la información que contiene. En este caso, el valor es el texto `"¡Hola mundo Python!"`.

El uso de variables agrega un poco más de trabajo para el intérprete. Cuando lee la primera línea, asocia la variable mensaje con el texto `"¡Hola mundo Python!"`. Cuando llega a la segunda línea, muestra en pantalla el valor asociado a mensaje.

Podemos ampliar este programa modificando `hello_world.py` para que imprima un segundo mensaje. Agrega una línea en blanco y luego dos nuevas líneas:
```python
mensaje = "¡Hola mundo Python!"
print(mensaje)

mensaje = "¡Hola mundo del curso intensivo de Python!"
print(mensaje)
```
Al ejecutar este programa, verás dos líneas:
```
¡Hola mundo Python!
¡Hola mundo del curso intensivo de Python!
```
Puedes cambiar el valor de una variable en cualquier momento, y Python siempre sabrá cuál es su valor más reciente.
### Nombrar y usar variables

Al usar variables en Python, debes seguir algunas reglas y buenas prácticas. Incumplir ciertas reglas causará errores; otras son recomendaciones para hacer tu código más legible y comprensible.

Sigue estas reglas al trabajar con variables:

    Los nombres de las variables solo pueden contener letras, números y guiones bajos (_). Deben comenzar con una letra o un guion bajo, pero no con un número. Por ejemplo, puedes usar mensaje_1, pero no 1_mensaje.

    No se permiten espacios en los nombres, pero puedes usar guiones bajos para separar palabras. Por ejemplo, mensaje_saludo es válido, pero mensaje saludo generará un error.

    Evita usar palabras clave de Python o nombres de funciones como variables. Por ejemplo, no uses print como nombre de variable, ya que está reservado. (Consulta "Palabras clave de Python y funciones integradas" en la página 466).

    Los nombres deben ser breves pero descriptivos. Por ejemplo, nombre es mejor que n, y nombre_estudiante es mejor que s_n.

    Ten cuidado con letras como la l minúscula y la O mayúscula, ya que pueden confundirse con los números 1 y 0.

Puede que necesites algo de práctica para encontrar buenos nombres de variables, especialmente a medida que tus programas se vuelvan más complejos. Con el tiempo y al leer código de otras personas, mejorarás en este aspecto.

    Nota: Las variables en Python, por convención, se escriben en minúsculas. Aunque no causa errores usar mayúsculas, estas se reservan para otros propósitos que veremos más adelante.

Evitar errores con nombres de variables

Todos los programadores cometen errores, incluso los más experimentados. Lo importante es aprender a identificarlos y resolverlos rápidamente.

Vamos a escribir un código que contenga un error intencional:

```python
mensaje = "¡Hola lector del curso intensivo de Python!"
imprmir(mensaje)
```

El resultado será un error. Python intenta ayudarte mostrando un rastreo que indica dónde ocurrió el problema. Este rastreo se ve así:

```
Traceback (most recent call last):
  File "hello_world.py", line 2, in <module>
    imprmir(mensaje)
NameError: name 'imprmir' is not defined. Did you mean: 'print'?
```
El error indica que en la línea 2 se ha usado una función llamada imprmir, que no está definida. Python incluso sugiere que quizás quisiste decir `print`.

Los errores de nombre suelen deberse a que olvidaste definir una variable o a errores tipográficos. Python no corrige tu ortografía, pero sí requiere que los nombres coincidan exactamente.

Por ejemplo:
```python
mensaje = "¡Hola lector del curso intensivo de Python!"
print(mensaje)
```

Este código se ejecuta correctamente. Los nombres coinciden exactamente, por lo que no hay problema.

Muchos errores de programación se deben a simples errores de escritura. ¡No te preocupes! A todos les pasa. Trata de tomarlo con humor y continúa. Aprenderás con la práctica.
Las variables son etiquetas

A menudo se describe a las variables como "cajas" que contienen valores. Esta idea puede ayudarte al principio, pero no es del todo precisa. Es mejor pensar en las variables como etiquetas que se asignan a valores.

Una variable hace referencia a un valor específico, y puedes cambiar esa referencia en cualquier momento.

    Nota: La mejor forma de aprender un nuevo concepto es usarlo. Si te atascas con un ejercicio, intenta hacer otra cosa por un momento, vuelve después o revisa el capítulo correspondiente. También puedes consultar el Apéndice C para obtener más sugerencias.

---
### INTÉNTALO TÚ MISMO

Escribe un programa separado para cada uno de estos ejercicios. Guarda cada archivo usando letras minúsculas y guiones bajos, como `mensaje_simple.py`.

2-1. Mensaje simple
Asigna un mensaje a una variable y luego imprime ese mensaje.

2-2. Mensajes simples
Asigna un mensaje a una variable e imprímelo. Luego cambia el valor de la variable por un nuevo mensaje e imprímelo de nuevo.

---

## Cadenas de texto

Como la mayoría de los programas definen y almacenan algún tipo de datos para luego hacer algo útil con ellos, es importante clasificar los diferentes tipos de datos. El primer tipo de datos que veremos es la cadena de texto `(string)`. Las cadenas parecen simples al principio, pero puedes usarlas de muchas maneras diferentes.

Una cadena es una secuencia de caracteres. Todo lo que esté entre comillas se considera una cadena en Python. Puedes usar comillas simples o dobles para definirlas:

```
"Esto es una cadena."
'Esto también es una cadena.'
```
Esta flexibilidad te permite usar comillas o apóstrofos dentro de las cadenas:

```
'Le dije a mi amigo: "¡Python es mi lenguaje favorito!"'
"El lenguaje 'Python' recibe su nombre de Monty Python, no de la serpiente."
"Una de las fortalezas de Python es su comunidad diversa y solidaria."
```

Exploremos algunas formas en las que puedes trabajar con cadenas de texto.

### Cambiar el uso de mayúsculas en una cadena con métodos

Una de las tareas más simples que puedes hacer con cadenas es cambiar el uso de mayúsculas y minúsculas en las palabras de una cadena. Observa el siguiente código e intenta entender qué está sucediendo:

```python
name.py

nombre = "ada lovelace"
print(nombre.title())
```

Guarda este archivo como `name.py` y ejecútalo. Deberías ver este resultado:

```
Ada Lovelace
```

En este ejemplo, la variable nombre hace referencia a la cadena en minúsculas "ada lovelace". El método `title()` aparece después de la variable dentro de la función `print()`. Un método es una acción que Python puede realizar sobre un dato. El punto `(.)` después de la variable en `nombre.title()` le indica a Python que ejecute el método `title()` sobre esa cadena.

Cada método va seguido de paréntesis, ya que a menudo requieren información adicional para funcionar. Esa información se proporciona dentro de los paréntesis. El método `title()` no necesita ningún dato adicional, por eso los paréntesis están vacíos.

El método `title()` convierte cada palabra de la cadena para que comience con una letra mayúscula y el resto en minúsculas. Esto es útil, ya que normalmente querrás tratar un nombre como una pieza única de información. Por ejemplo, podrías querer que tu programa reconozca "Ada", "ADA" y "ada" como el mismo nombre y los muestre todos como "Ada".

También existen otros métodos útiles para trabajar con el uso de mayúsculas:

```python
nombre = "Ada Lovelace"
print(nombre.upper())
print(nombre.lower())
```

Esto mostrará lo siguiente:
```
ADA LOVELACE
ada lovelace
```

El método `lower()` es especialmente útil cuando se almacenan datos. Generalmente, no querrás depender del uso de mayúsculas que proporcionan los usuarios, por lo que convertirás las cadenas a minúsculas antes de almacenarlas. Luego, cuando muestres la información, puedes aplicar el formato que tenga más sentido.

### Usar variables en cadenas

En algunas situaciones, querrás incluir el valor de una variable dentro de una cadena.
Por ejemplo, podrías usar dos variables para representar un nombre y un apellido por separado, y luego combinarlas para mostrar el nombre completo de alguien:


nombre_completo.py
```python
primer_nombre = "ada"
apellido = "lovelace"
nombre_completo = f"{primer_nombre} {apellido}"
print(nombre_completo)
```
Para insertar el valor de una variable dentro de una cadena, coloca una letra `f` justo antes de las comillas que abren la cadena. Luego, encierra entre llaves `({})` el nombre de la variable que quieras incluir. Python reemplazará esas llaves por el valor actual de la variable al momento de mostrar la cadena.

Estas se conocen como `f-strings` (formatted strings o cadenas formateadas). La `f` indica que Python debe formatear la cadena sustituyendo el nombre de cualquier variable entre llaves por su valor.
El resultado del código anterior será:

```
ada lovelace
```

Las `f-strings` te permiten construir mensajes completos fácilmente a partir de valores almacenados en variables. Por ejemplo:

```python
primer_nombre = "ada"
apellido = "lovelace"
nombre_completo = f"{primer_nombre} {apellido}"
print(f"Hola, {nombre_completo.title()}!")
```
Aquí, el nombre completo se incluye dentro de una oración que saluda al usuario, y el método `title()` cambia el nombre a formato título (mayúscula inicial en cada palabra).
Este código muestra:

```
Hola, Ada Lovelace!
```

También puedes usar `f-strings` para construir el mensaje completo y luego asignarlo a una variable:

```python
primer_nombre = "ada"
apellido = "lovelace"
nombre_completo = f"{primer_nombre} {apellido}"
mensaje = f"Hola, {nombre_completo.title()}!"
print(mensaje)
```

Este código también mostrará:

```
Hola, Ada Lovelace!
```

Pero al asignar el mensaje a una variable, se simplifica la llamada final a `print()`.

### Agregar espacios en blanco a cadenas con tabulaciones o saltos de línea

En programación, los espacios en blanco se refieren a cualquier carácter no visible, como espacios, tabulaciones `(\t)` y saltos de línea `(\n)`. Puedes usar espacios en blanco para organizar la salida del programa de una forma más legible para el usuario.

Para agregar una tabulación a tu texto, usa la combinación de caracteres `\t`:

```python
print("Python")
print("\tPython")
```
Esto mostrará:
```
Python
	Python
```
Para insertar un salto de línea, usa la combinación de caracteres `\n`:

```python
print("Lenguajes:\nPython\nC\nJavaScript")
```

Esto mostrará:
```
Lenguajes:
Python
C
JavaScript
```

También puedes combinar tabulaciones y saltos de línea en una sola cadena. Por ejemplo, `\n\t` le indica a Python que agregue un salto de línea y luego una tabulación en la nueva línea:

```python
print("Lenguajes:\n\tPython\n\tC\n\tJavaScript")
```

Esto mostrará:
```
Lenguajes:
	Python
	C
	JavaScript
```

Las tabulaciones y los saltos de línea serán muy útiles en los próximos capítulos, cuando empieces a generar múltiples líneas de salida a partir de unas pocas líneas de código.

### Eliminación de espacios en blanco

Los espacios en blanco adicionales pueden causar confusión en tus programas.
Para una persona, `'python'` y `'python '` (con un espacio al final) pueden parecer iguales.
Pero para Python, son dos cadenas diferentes. Python detecta el espacio extra en `'python '` y lo considera parte significativa de la cadena, a menos que le indiques lo contrario.

Es importante tener en cuenta los espacios en blanco, ya que a menudo necesitarás comparar cadenas para saber si son iguales. Un ejemplo común sería verificar los nombres de usuario cuando las personas inician sesión en un sitio web. También pueden causar problemas en situaciones más simples.

Afortunadamente, Python hace que sea fácil eliminar espacios en blanco adicionales que los usuarios puedan ingresar.
Eliminar espacios en blanco del lado derecho

Python puede eliminar los espacios en blanco que están al final de una cadena con el método `rstrip()`:

```shell
>>> idioma_favorito = 'python '
>>> idioma_favorito
'python '
>>> idioma_favorito.rstrip()
'python'
>>> idioma_favorito
'python '
```

En este ejemplo, la variable `idioma_favorito` contiene un espacio extra al final.

Cuando usamos `rstrip()`, Python devuelve una versión de la cadena sin ese espacio final.

Pero el valor original no cambia, a menos que lo actualices tú mismo.

### Eliminar espacios de forma permanente

Para eliminar el espacio en blanco de forma permanente, asigna el resultado de `rstrip()` de nuevo a la variable:

```shell
>>> idioma_favorito = 'python '
>>> idioma_favorito = idioma_favorito.rstrip()
>>> idioma_favorito
'python'
```

Este patrón —actualizar una variable con una versión modificada de sí misma— es muy común en programación. Se usa tanto para cambiar valores como para responder a la entrada del usuario.
Eliminar espacios del lado izquierdo y de ambos lados

Además de `rstrip()`, puedes usar `lstrip()` para eliminar espacios al inicio de la cadena, o `strip()` para eliminar espacios en ambos extremos:

```shell
>>> idioma_favorito = ' python '
>>> idioma_favorito.rstrip()
' python'
>>> idioma_favorito.lstrip()
'python '
>>> idioma_favorito.strip()
'python'
```

El valor inicial tiene espacios en blanco antes y después.

Usamos `rstrip()` para quitar solo el del final, `lstrip()` para quitar solo el del inicio, y `strip()` para quitar ambos.

Experimentar con estos métodos de eliminación `(strip, rstrip, lstrip)` te ayudará a familiarizarte con la manipulación de cadenas.
En la práctica, estos métodos se usan principalmente para limpiar la entrada del usuario antes de almacenarla o procesarla.

### Eliminación de prefijos

Cuando trabajas con cadenas, otra tarea común es eliminar un prefijo.
Por ejemplo, considera una URL que empieza con el prefijo común `https://`.
Queremos eliminar ese prefijo para enfocarnos solo en la parte que los usuarios deben escribir en la barra de direcciones. Así es como puedes hacerlo:

```shell
>>> nostarch_url = 'https://nostarch.com'
>>> nostarch_url.removeprefix('https://')
'nostarch.com'
```

Escribe el nombre de la variable, seguido de un punto (.), y luego el método `removeprefix()`. Dentro de los paréntesis, coloca el prefijo que deseas quitar de la cadena original.

Al igual que los métodos para eliminar espacios en blanco, `removeprefix()` no modifica la cadena original. Si quieres conservar el valor sin el prefijo, debes asignarlo a una nueva variable o reasignarlo a la misma:

```shell
>>> simple_url = nostarch_url.removeprefix('https://')
```
Cuando ves una URL en la barra de direcciones del navegador y no aparece la parte `https://`, probablemente el navegador esté usando internamente un método como `removeprefix()`.

### Evitar errores de sintaxis con cadenas

Un error común en Python es el error de sintaxis, que ocurre cuando Python no reconoce una parte del código como válida.
Por ejemplo, si usas una comilla simple dentro de una cadena encerrada también con comillas simples, obtendrás un error. Esto sucede porque Python cree que la cadena termina en la primera comilla simple, e intenta interpretar el resto como código, lo que produce un error.

Aquí te mostramos cómo manejar correctamente comillas simples y dobles. Guarda este archivo como `apostrophe.py` y ejecútalo:

```python
message = "Una de las fortalezas de Python es su comunidad diversa."
print(message)
```

El apóstrofe está dentro de comillas dobles, así que Python interpreta la cadena correctamente:
```
Una de las fortalezas de Python es su comunidad diversa.
```

Pero si usas comillas simples:

```python
message = 'Una de las fortalezas de Python es su comunidad diversa.'
print(message)
```
Verás un error como este:

```shell
Archivo "apostrophe.py", línea 1
message = 'Una de las fortalezas de Python es su comunidad diversa.'
                                    ^
SyntaxError: cadena de texto sin cerrar correctamente
```
Este error indica que Python no pudo entender dónde empieza y termina la cadena.

💡 Consejo: La función de resaltado de sintaxis de tu editor puede ayudarte a detectar estos errores. Si ves que el texto se resalta como si fuera inglés normal o partes del código aparecen como si fueran texto, puede que tengas comillas desbalanceadas.

---
### PRUÉBALO TÚ MISMO

Guarda cada uno de los siguientes ejercicios como un archivo por separado, con nombres como `nombre_casos.py`. Si te atoras, toma un descanso o revisa las sugerencias del Apéndice C.

2-3. Mensaje personal
Usa una variable para representar el nombre de una persona e imprime un mensaje para esa persona.
Tu mensaje debe ser algo simple, como:

    "Hola Eric, ¿te gustaría aprender algo de Python hoy?"

2-4. Casos del nombre
Usa una variable para representar el nombre de una persona y luego imprime el nombre en minúsculas, mayúsculas y formato título.

2-5. Cita famosa
Busca una cita de una persona famosa que admires. Imprime la cita y el nombre del autor.
El resultado debe verse así (incluyendo las comillas):

    Albert Einstein dijo una vez: "Una persona que nunca cometió un error nunca intentó algo nuevo."

2-6. Cita famosa 2
Repite el ejercicio 2-5, pero esta vez guarda el nombre del autor en una variable llamada persona_famosa, y luego guarda el mensaje completo en una variable llamada mensaje. Imprime el mensaje.

2-7. Eliminación de espacios
Usa una variable para representar el nombre de una persona, agregando espacios en blanco antes y después del nombre.
Asegúrate de usar al menos una vez los caracteres "\t" y "\n".
Imprime el nombre para mostrar los espacios, y luego usa las funciones lstrip(), rstrip() y strip() para eliminar los espacios de diferentes formas.

2-8. Extensiones de archivo
Python tiene un método llamado removesuffix() que funciona igual que removeprefix().
Asigna 'python_notes.txt' a una variable llamada nombre_archivo, y luego usa removesuffix() para mostrar el nombre del archivo sin la extensión, como hacen algunos exploradores de archivos.

---

## Números

Los números se usan con frecuencia en programación: para llevar la puntuación en juegos, representar datos en gráficas, almacenar información en aplicaciones web, y mucho más.
Python trabaja con números de diferentes formas, dependiendo de cómo se usen. Vamos a empezar con los números enteros, que son los más sencillos.

### Enteros

Puedes usar los operadores estándar de suma (+), resta (-), multiplicación (*) y división (/) con números enteros en Python:

```
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 6
12
>>> 3 / 2
1.5
```

En una sesión interactiva, Python simplemente devuelve el resultado de la operación.

Python también usa dos símbolos de multiplicación para representar exponentes:

```
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

Python respeta el orden de las operaciones matemáticas, así que puedes combinar varias operaciones en una sola expresión:

```
>>> 2 + 3 * 4
14
>>> (2 + 3) * 4
20
```

Los espacios no afectan cómo se evalúa la expresión; simplemente ayudan a que el código sea más fácil de leer.

### Flotantes

Un número con un punto decimal se llama flotante o `(float)`.
Este término es común en la mayoría de los lenguajes de programación y se refiere a que el punto decimal puede "flotar", es decir, aparecer en cualquier parte del número.

Python maneja bien los flotantes, así que generalmente no tendrás que preocuparte por cómo se comportan:

```
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

Sin embargo, a veces verás un resultado con más decimales de los esperados:

```shell
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

Esto es normal en todos los lenguajes de programación y no debería preocuparte por ahora.
Más adelante, en la Parte II del libro, aprenderás cómo controlar mejor la precisión decimal si lo necesitas.

### Enteros y flotantes juntos

Cuando divides dos números, aunque sean enteros y el resultado sea entero, Python devuelve un flotante:

```
>>> 4 / 2
2.0
```

Si mezclas enteros y flotantes en cualquier otra operación, también obtendrás un flotante:

```
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

Python convierte automáticamente el resultado en flotante si algún número de la operación lo es.

### Guiones bajos en números

Cuando trabajas con números grandes, puedes usar guiones bajos (_) para agrupar los dígitos y hacerlos más legibles:

```
>>> edad_universo = 14_000_000_000
>>> print(edad_universo)
14000000000
```

Python ignora los guiones bajos al almacenar el valor.
Puedes agrupar los dígitos como quieras: 1_000 es lo mismo que 10_00 o 1000 para Python.
Esta característica funciona tanto para enteros como para flotantes.

### Asignación múltiple

Puedes asignar valores a varias variables en una sola línea, lo cual hace el código más limpio y legible. Por ejemplo:

```
>>> x, y, z = 0, 0, 0
```

Simplemente separa los nombres de las variables con comas, y haz lo mismo con los valores.
Python se encarga de emparejarlos correctamente, siempre que la cantidad de variables y valores coincida.

### Constantes

Una constante es una variable cuyo valor no debería cambiar durante la ejecución del programa.

Python no tiene constantes integradas como otros lenguajes, pero por convención, los programadores escriben los nombres de las constantes en mayúsculas:

```
MAX_CONEXIONES = 5000
```

Si ves una variable con nombre en mayúsculas, eso indica que su valor no debe modificarse.

---
### PRUÉBALO TÚ MISMO

2-9. Número ocho
Escribe operaciones de suma, resta, multiplicación y división que den como resultado el número 8.
Usa print() para mostrar el resultado.
Tu código debería incluir cuatro líneas como esta:

print(5 + 3)

Y la salida debe mostrar el número 8 una vez en cada línea.

2-10. Número favorito
Usa una variable para representar tu número favorito.
Luego, crea un mensaje que revele ese número y muestra el mensaje con print().

---

## Comentarios

Los comentarios son una herramienta extremadamente útil en la mayoría de los lenguajes de programación. Hasta ahora, todo lo que has escrito en tus programas ha sido código Python. Pero a medida que tus programas se vuelvan más largos y complejos, necesitarás agregar notas dentro de ellos que describan tu enfoque general al resolver un problema.
Un comentario te permite escribir estas notas en lenguaje natural, dentro del propio código.

### ¿Cómo se escriben comentarios?

En Python, el símbolo de almohadilla `(#)` indica un comentario.
El intérprete de Python ignora todo lo que venga después de este símbolo en una línea.

Por ejemplo, el archivo `comment.py` podría verse así:

```python
# Saluda a todos.
print("¡Hola gente de Python!")
```

Python ignora la primera línea (el comentario) y ejecuta la segunda:

```
¡Hola gente de Python!
```

### ¿Qué tipo de comentarios deberías escribir?

La razón principal para escribir comentarios es explicar qué hace tu código y cómo lo hace.
Cuando estás trabajando activamente en un proyecto, todo tiene sentido porque tienes el contexto en mente. Pero si vuelves a ese mismo código semanas o meses después, es muy probable que olvides muchos detalles.

Aunque puedes analizar el código para recordar cómo funciona, escribir buenos comentarios te ahorrará tiempo al resumir claramente tu lógica y tus decisiones.

Si quieres convertirte en un programador profesional o colaborar con otras personas, necesitas escribir comentarios significativos. Hoy en día, la mayoría del software se desarrolla de forma colaborativa, ya sea por equipos dentro de una empresa o por comunidades de código abierto.

Los programadores experimentados esperan encontrar comentarios en el código, así que es buena idea empezar desde ahora a incluirlos.
Comentar tu código de forma clara y concisa es uno de los mejores hábitos que puedes desarrollar como programador principiante.

Cuando dudes si vale la pena escribir un comentario, pregúntate:

    ¿Tuve que pensar en varias formas de resolver esto antes de encontrar una solución que funcionara?

Si la respuesta es sí, escribe un comentario explicando tu razonamiento.
Siempre es más fácil eliminar comentarios innecesarios más adelante que tener que reconstruir la lógica de un código sin comentar.

A partir de ahora, este libro incluirá comentarios en los ejemplos para ayudarte a entender mejor cada sección de código.

---
### PRUÉBALO TÚ MISMO

2-11. Agrega comentarios
Elige dos de los programas que hayas escrito y agrega al menos un comentario en cada uno.
Si tus programas son muy simples y no tienes nada específico que explicar aún, escribe tu nombre y la fecha actual en la parte superior de cada archivo, y una frase que describa qué hace el programa.

---
### El Zen de Python

Los programadores experimentados de Python suelen promover la simplicidad por encima de la complejidad.
La filosofía de la comunidad de Python está resumida en un breve texto llamado "El Zen de Python", escrito por Tim Peters.

Puedes leerlo escribiendo lo siguiente en el intérprete de Python:

```
import this
```
No lo reproduciremos completo aquí, pero compartiremos algunas líneas clave para ayudarte a comprender por qué esta filosofía es importante para ti como nuevo programador de Python:

#### The Zen of Python, by Tim Peters

Lo bello es mejor que lo feo.

Los programadores de Python creen que el código puede ser bello y elegante.
En programación, resolvemos problemas, y las soluciones bien diseñadas, eficientes e incluso hermosas siempre han sido valoradas.

A medida que escribas más código en Python, quizás alguien lo vea y diga:

    “¡Guau, qué código tan hermoso!”

Lo simple es mejor que lo complejo.

Si tienes que elegir entre una solución simple y una compleja (y ambas funcionan), usa la simple.
Será más fácil de mantener y más fácil de entender para ti y para otros.

Lo complejo es mejor que lo complicado.

A veces, los problemas del mundo real no pueden resolverse de forma sencilla. En esos casos, usa la solución más sencilla posible que funcione.

La legibilidad cuenta.

Incluso cuando tu código sea complejo, intenta que sea legible.
Si trabajas en un proyecto que requiere código complicado, asegúrate de escribir comentarios informativos para que otros puedan entenderlo fácilmente.

Debe haber una (y preferiblemente solo una) forma obvia de hacerlo.

Cuando dos programadores de Python intentan resolver el mismo problema, deberían encontrar soluciones similares.
Esto no significa que no haya espacio para la creatividad; ¡hay mucho!
Pero en general, los buenos programas se construyen usando enfoques comunes y claros dentro de proyectos más grandes y creativos.

Ahora es mejor que nunca.

Podrías pasar años aprendiendo todos los detalles de Python, pero nunca terminarías un proyecto.
No esperes a saberlo todo para empezar. Escribe código que funcione, y después decide si lo mejorarás o pasarás a algo nuevo.
 
---
### PRUÉBALO TÚ MISMO

2-12. El Zen de Python
Abre una terminal interactiva de Python, escribe import this y lee todos los principios del Zen de Python.
Reflexiona sobre cómo pueden ayudarte a escribir mejor código.

---

## Resumen

En este capítulo aprendiste a:

    Usar variables con nombres descriptivos.

    Resolver errores comunes de nombre y sintaxis.

    Trabajar con cadenas de texto, usarlas en minúsculas, mayúsculas y formato título.

    Utilizar espacios en blanco para organizar la salida.

    Eliminar espacios innecesarios de las cadenas.

    Trabajar con números enteros y flotantes, y realizar operaciones matemáticas.

    Escribir comentarios explicativos para que tu código sea más claro para ti y para otros.

    Adoptar la filosofía de simplicidad y claridad en la programación.

En el Capítulo 3, aprenderás a almacenar colecciones de información usando una estructura llamada listas, y a manipular cualquier dato dentro de ellas.
