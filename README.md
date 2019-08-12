# Análisis de dominios de correo

En este proyecto se analizará un archivo `.csv`
el cual contiene 257 correos registrados, cada uno
con un dominio distinto.
Dicho conjunto de datos fué extraido de la siguiente
página: [Lista](https://sites.google.com/site/gruposcoutsanbruno1/principal/noticias/lista-actualizada-mails)

## Requerimientos.
-	Python3.x
- 	matlibplot 

Para instalar la libreria de matlibplot en es necesario 
instalar el gestor de paquetes de python3 --> `pip3`

Después de ello simplemente instalamos matlibplot:


```bash
$ pip3 install matplotlib

```

## Datos usados

![Dataset](https://github.com/Kevincastillo98/Analisis_Correos/blob/master/Imagenes/Correos.png)

## Desarrollo

Para poder hacer el análisis de patrones en una cadena 
de texto, podemos utilizar `regex`  o expresiones regulares, las cuales nos facilitarán la busqueda de los dominios de correo,para ello importaremos la libreria `re` en python.

```python
import re
``` 

Para poder generar un gráfico a partir de los datos obtenidos
importaremos la libreria matplotlib.

```python
import matplotlib.pyplot as plt
```

Para abrir un archivo de texto en python , basta usar la
funcion `open("nombre_del_archivo,"Formato_de_apertura"")`

- `r = read`
- `w = write`

```python 
texto = open("emails.csv","r")
```
Ahora nos interesa buscar todas las cadenas de texto que
incluyan al caracter `@` para ello mandamos llamar al método
`findall` de la libreria `re`, los parámetros de dicha función son los siguientes:  `re.findall("caracter_a_buscar",archivo)`

```python
emails = re.findall("@.*",texto)
```



## Salida

![Diccionario](https://github.com/Kevincastillo98/Analisis_Correos/blob/master/Imagenes/Diccionario.png)

## Gráfica

![Grafica](https://github.com/Kevincastillo98/Analisis_Correos/blob/master/Imagenes/Grafica.png)

