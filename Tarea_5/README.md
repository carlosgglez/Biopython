# Buscar el accesion de UniProt

Este script de Python tiene dos funciones, utilizando las bibliotecas de "Biopython" y el módulo "Entrez" 
para interactuar con la base de datos "Protein" del NCBI. La primera función realiza una búsqueda para
encontrar proteínas relacionadas al gen DEFA en el mosquiro Aedes aegypti
e imprime en pantalla los IDs que coinciden con el término de la búsqueda.

La segunda función selecciona el primer ID y realiza una búsqueda en 
"GeneBank" e imprime información detallada acerca de esta.

## Uso

Solo se debe de correr en una terminal que use python.

## Salida

Imprime en pantalla los Id's relacionados al gen DEFA del mosquito *Aedes aegypti* que se encontraron 
en la base de datos de protein.
Después, imprime también en pantalla el GenBak de la proteina codificada por dicho gen.

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
