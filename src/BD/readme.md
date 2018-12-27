Mapeos:

Métodos:

    * constructor: construye una instancia de la clase (no interactua con la base de datos)
    * newNombre_Clase: construye una instancia de la clase y inserta los valores en la base de datos (si no estan en la misma)
    se hacen las comprobaciones de integridad
    * getNombre_Clase: método estatico que recibiendo como parametro el valor de la clave primaria de la tabla crea una instancia de la clase con los valores de esa tupla
    
    * en el caso de las clases foraneas en la instancia se crea una instancia de ese atributo (por ejemplo en la tabla Colegio hay un atributo
    Colonia que es clave foranea de la tabla colonia, por lo que cuando se crea una instancia de Colegio se crea una de la clase colonia)

    * getters: devuelven el valor del atributo de la instancia (en el caso de las claves foraneas el getNombreAtributo devuelve una instancia
    de la clase de la clave foranea y el getNombreAtributoId devuelve el id de la clase de la clave foranea)

    * setters: permiten modificar el valor de los atributos tanto en la instancia como en la base de datos (se realiza controles de integridad
    de los datos)

    * listaNombreClase: método estatico que toma los valores de la base de datos y crea una lista de instancias

    * delete: permite borrar una tupla de la base de datos y pone en nulo todos los valores de la instancia

    * repr: permite la representación de la instancia