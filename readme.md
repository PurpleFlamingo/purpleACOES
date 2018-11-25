# PurpleACOES

Para conectar con la base de datos, modificar el archivo `src/BD/database.config` con la informacion de la base de datos, usuario y contrasena.

**No hagais ningun commit/push de ese archivo.**



Informacion variada:

* En la carpeta `src` iremos metiendo el codigo que vaya a ser usado en la entrega final, pruebas y demas iran a la carpeta `pruebas`

* Dentro de `src` todos los archivos `*.ui` , iran a la carpeta `src/UI`

* No usar espacios ni caracteres especiales en los nombres de los archivos. En vez de espacios usar camel case (porEjemploSeEscribiriaAsi.png)

* Para el desarrollo en python os recomiendo usar virtualenv, os crea una instalacion privada de python para no mezclar modulos instalados con otros proyectos en vuestro equipo y evitar errores inesperados, pero no es obligatorio

* Para instalar todas las depencias necesarias bastara con hacer un `pip install -r requirements.txt` si en algun momento anadimos librerias nuevas al proyecto deberiamos actualizar el archivo con un `pip freeze`

* Si cambiais la extensión de los script de python de .py a .pyw no aparece la consola.

Inicio de sesión
El funcionamiento del botón login es:
     * si el nombre de usuario o la contraseña están vacíos, no hace nada
     * en caso contrario paso al método inicio_sesión el nombre de usario y la contraseña
     * inicio_sesión se conecta con la base de datos y  solicita en la tabla usuario la contraseña de ese usuario
     * si el usuario no existe (se recibe una tupla vacia de la consulta) o la contraseña que se introdujo es erronea el método devuelve falso
     * si el usuario existe y la contraseña es correcta el método devuelve verdadero
     * al recibir la respuesta del método, si esta es verdadera, se reinicia el conteo de intentos erroneos y se inicia la aplicacion
     * si se recibe una respuesta falsa, se incrementa en uno el conteo de intentos erroneos y si es menor de 5 se muestra un mensaje
     * y si ese conteo es 5 se muestra un cuadro de dialogo, que bloqua la ventana de inicio de sesión y que solo tiene un botón que 
cierra la aplicacion.
