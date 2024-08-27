# E.search

Este script de Python tiene dos funcionalidades, en ambas se utilizan las bibliotecas de "Biopython" y de "Entrez".
Su primera funcionalidad sirve para hacer una consulta en la base de datos de "Protein", regresando la descripción del FieldList "ECNO" y la descripción del
LinklList "protein_protein_small_genome".
        
La otra función que tiene el prgrama es de buscar en la base de 
datos de Pubmed las entradas que hay de la Doctora Constance Auvynet,
especificando encontrar los artículos que en el titulo mencionen algo
sobre "peptide", "antimicrobial" o "migration".

## Uso

Solo se debe de correr en una terminal en la cual se pueda utilizar python.

## Salida

Imprime en pantalla la descripción del FieldList "ECNO" y la descripción del LinkList de "protein_protein_small_genome".
También, genera un archivo llamado "Ids_Constance_Auvynet.md" el cual es un archivo de texto plano con extensión md o MarkDown.

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