# E.search

Fecha: 10/08/2024

**Participantes**
Carlos García González <email: carlosgg@lcg.unam.mx>


## Descripción del Problema

El tiempo al momento de hacer una consulta en una base de datos es crucial, ya que, si bien no es mucho, se puede optimizar cuando se tienen que realizar muchas, por lo cual se desarrollo este script, tiene la finalidad de que se 
puedan hacer las cosultas de una manera más rapida y ágil.


## Especificación de Requisitos

Requisitos no funcionales

- El script debe de estar escrito en Python
- El tiempo de respuesta debe de ser rápido, incluso si se hace una consulta grande


## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

'''
from Bio import Entrez
from pprint import pprint  # Mejor visualización de diccionarios
Entrez.email = "carlosgg@lcg.unam.mx"

handle = Entrez.einfo(db="pubmed")
record = Entrez.read(handle)

for field in record["DbInfo"]["FieldList"]:
    print(field["Name"] + "," + field["FullName"] + "," + field["Description"])

print("\nURL de la consulta:", handle.url)

primer_campo = record['DbInfo']['FieldList'][0]
print("\nDescripción del primer campo:")
print(primer_campo["Description"])

handle.close()

'''




