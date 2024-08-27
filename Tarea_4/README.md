# E.search

Este script de Python realiza tres funciones utilizando la biblioteca de “Biopython” y “Entrez” para interactuar con la base de datos de PubMed. 

La primera función  busca artículos de la Dra. Constance Auvynete, utilizando ciertas palabras clave (en este caso se usan "peptide" o "antimicrobial" o "migration") del título, límita la busqueda a 100 resultados e imprime en pantalla los IDs de los artículos que coinciden con el término de la búsqueda. 

La segunda función recupera los abstracts (resúmenes) de los artículos que coinciden y los guarda en un archivo. La tercera y última función  busca artículos en PubMed que citen a los artículos encontrados en la búsqueda inicial, los IDs de los artículos citantes se extraen y se almacenan en un archivo.  


## Uso

Solo se debe de correr en una terminal en la cual se pueda utilizar python.

## Salida

Imprime en pantalla los IDs de los artículos que coinciden con el término de la búsqueda (limita sólo a 100 resultados). 

También, genera un archivo llamado "Abstracts_Constance_Auvynet.md" el cual es un archivo de texto plano con extensión md o MarkDown en el cual se recopilan los abstracts de los artículos que concidieron con la búsqueda.

Además, extrae los IDs de artículos citantes y los almacena en una lista llamada "Citations_Constance_Auvynet.txt", el cual es un archivo de texto plano con extensión txt.

## Pruebas

El script incluye un conjunto depruebas unitarias que se pueden checar en la carpeta de "test".

## Datos

No es necesario darle ningún archivo al script para que funcione.

## Metadatos y documentacion

Este README ofrece información de uso básico. Para obtener información más detallada sobre el diseño y la implementación del script favor de mandar un correo a la siguiente dirección:

<email: carlosgg@lcg.unam.mx>

## Codigo fuente

El código fuente está disponible en este repositorio. Se acoge con satisfacción cualquier contribución o sugerencia a través de solicitudes pull request.

## Terminos de uso

Este script está disponible bajo la licencia MIT license. Consulte el archivo LICENSE para obtener más detalles.

## Como citar

Si utiliza este script en su trabajo, por favor citelo.

## Contactenos

Carlos García González 
<email: carlosgg@lcg.unam.mx>
