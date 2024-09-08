# Buscar el accesion de UniProt

Fecha: 26/08/2024

**Participantes**
Carlos García González <email: carlosgg@lcg.unam.mx>


## Descripción del Problema

El programa tiene como objetivo buscar y recuperar información sobre proteínas específicas en la base de datos de NCBI utilizando el 
módulo Bio.Entrez de Biopython. Más específicamente:

Búsqueda de Proteínas: El problema que resuelve el programa es encontrar el ID de una proteína para un gen específico en una base de datos de proteínas, 
en este caso, utilizando términos de búsqueda relacionados con el gen DEFA en Aedes aegypti.

Recuperación de Información: Una vez que se encuentra el ID de la proteína, el programa extrae el registro completo de esa proteína desde la base de 
datos de proteínas (en formato GenBank). Esto incluye detalles como la secuencia de la proteína, anotaciones y otras informaciones relevantes.


## Especificación de Requisitos

Requisitos no funcionales

- El script debe de estar escrito en Python
- El tiempo de respuesta debe de ser rápido, incluso si se hace una consulta grande


## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

'''
from Bio import Entrez
from pprint import pprint

Entrez.email = "carlosgg@lcg.unam.mx"

handle = Entrez.esearch(db = "protein", term = "DEFA[Aedes aegypti]")
record = Entrez.read(handle)

print("Lista de Id's la informacion del gen DEFA del mosquito en la db de protein: ")
print(record["IdList"])

prot_id = record["IdList"][0]

handle = Entrez.efetch(db = "protein", id = prot_id, rettype = "gb", retmode = "text")
genbank_record = handle.read()
handle.close()

print(genbank_record)
'''




