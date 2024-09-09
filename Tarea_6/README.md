# BLAST

Este script de Python tiene dos funciones, utilizando la biblioteca
de "Biopython" y los módulos "SeqIO", "NCBIWWW" y "NCBIXML" para interactuar
con la base de datos "nr" del NCBI. La primera función carga un archivo fasta 
que contiene una única secuencia, después realiza una busqueda BLAST en la base 
de datos nr y por último filtra y muestra alineamientos cuyo valor E es menor que 0.05.

La segunda función también carga un archivo fasta, pero este, a diferencia del primero,
contiene multiples secuencias, para cada secuencia, realiza una búsqueda BLAST y encuentra
el alineamiento con el mejor score y cuyo valor E sea menor que 0.05.
Si encuentra un alineamiento significativo, imprime sus detalles. Si no, informa que no hay
alineamientos con un valor E dentro del umbral.

## Uso

Se debe de correr en una terminal que use python, y además el programa debe de estar en la  misma carpeta que los archivos opuntia1.fasta y opuntia.fasta

## Salida

Imprime en pantalla los alineamientos más significativos que encontro, estos alineamientos
tienen un E value menor a .05, la secuencia query es obtenida por medio de los archivos opuntia1.fasta y opuntia.


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
