# E.search

Fecha: 10/08/2024

**Participantes**
Carlos García González <email: carlosgg@lcg.unam.mx>


## Descripción del Problema

El problema principal a resolver es realizar una busqueda avanzada con etiquetas especificas, para despues generar un archivo a partir de segmentos de dichos datos y ese archivo que realize un busquedda inversa de citas que se le hayan realizado a los datos.

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

handle = Entrez.einfo(db="protein")
record = Entrez.read(handle)

ECNO_campo = record['DbInfo']['FieldList'][16]
print("\nDescripción del campo ECNO:")
print(ECNO_campo["Description"])

print("\nURL de la consulta:", handle.url)

protein_campo = record['DbInfo']['LinkList'][33]
print("\nDescripción del campo protein_protein_small_genome:")
print(protein_campo["Description"])

filename = "Id's_Constance_Auvynet.md"

termino = "(Auvynet-C[AUTH]) AND ((peptide[TITLE] OR peptides[TITLE]) OR (antimicrobial[TITLE] OR migration[TITLE]))"

handle = Entrez.esearch(db="pubmed", term=termino, retmax=100)
record = Entrez.read(handle)

archivo_salida = "Ids_Constance_Auvynet.md"
with open(archivo_salida, "w") as file:
    file.write("\n".join(record["IdList"]))

print(f"\nIDs guardados en {archivo_salida}")

handle.close()

'''




