# calendarios-astronomicos

Calendarios astronómicos es un conversor de fechas con capacidad de transformar las fechas del calendario gregoriano al calendario judío, al calendario musulmán y a la data juliana. También devuelve la fecha en formato ISO-8061. Forma parte de un TFG del Grado en Matemáticas de la Universidad de Santiago de Compostela.

# Instalación

> Requiere Python>=3.8

Primero de todo, tenemos que clonar el repositorio:

```
$ git clone https://github.com/poure13/calendarios-astronomicos
```

Despues accedemos a la carpeta e instalamos los requisitos del programa:

```
$ cd calendarios-astronomicos
$ pip install -r requirements.txt 
```

# Uso

Para ejecutar calendarios-astronomicos, simplemente hay que usar:

```
$ python calendarios-astronomicos.py
```

En caso de querer invocar la versión web:

```
$ python calendarios-astronomicos.py web
```

También está disponible un pequeño comando de ayuda:

```
$ python calendarios-astronomicos.py help               
Descripción: 

calendarios-astronomicos es un conversor de fechas con capacidad de transformar las fechas del calendario gregoriano al calendario judío, al calendario musulmán y a la data juliana. También devuelve la fecha en formato ISO-8061.
  
Argumentos:

  web       Crea un servicio web para acceder de forma más cómoda al conversor.
  help      Muestra este mensaje de ayuda.
```
