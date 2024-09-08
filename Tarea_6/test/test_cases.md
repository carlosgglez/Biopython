# Casos de prueba o escenarios

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

El objetivo de este archivo es validar y garantizar que el script funciona correctamente y cumple especificaciónes. 
Al ser este un script que no necesita de la intervención del usuario, no hay casos de prueba que se deban de necesitar para su funcionamiento.
