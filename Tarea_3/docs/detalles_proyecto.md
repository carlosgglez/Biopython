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

# Configuración del correo electrónico para Entrez (requerido por NCBI)
Entrez.email = "carlosgg@lcg.unam.mx"

# Obtención de ID y linaje de Notoryctes typhlops
handle = Entrez.esearch(db="Taxonomy", term="Notoryctes typhlops")
record = Entrez.read(handle)
print("El Id de Notoryctes typhlops es: ")
print(record["IdList"])

Id_Notoryctes = record["IdList"]
handle = Entrez.efetch(db="Taxonomy", id=Id_Notoryctes, retmode="xml")
Notoryctes = Entrez.read(handle)

# Obtención de ID y linaje de Chrysochloris asiatica
handle = Entrez.esearch(db="Taxonomy", term="Chrysochloris asiatica")
record = Entrez.read(handle)
print(f"\nEl Id de Chrysochloris asiatica es: ")
print(record["IdList"])

Id_Chryso = record["IdList"]
handle = Entrez.efetch(db="Taxonomy", id=Id_Chryso, retmode="xml")
Chryso = Entrez.read(handle)

# Impresión de linajes
print(f"\nLinaje de Notoryctes typhlops:")
linaje_Notoryctes = Notoryctes[0]["Lineage"].split("; ")
print(" > ".join(linaje_Notoryctes))

print(f"\nLinaje de Chrysochloris asiatica:")
linaje_Chryso = Chryso[0]["Lineage"].split("; ")
print(" > ".join(linaje_Chryso))

# Revisión automática de divergencia en linajes
for i in range(min(len(linaje_Notoryctes), len(linaje_Chryso))):
    if linaje_Notoryctes[i] != linaje_Chryso[i]:
        print(f"\nLos linajes de Notoryctes typhlops y Chrysochloris asiatica divergen después de ser ambos {linaje_Notoryctes[i-1]}.")
        print(f"Notoryctes es {linaje_Notoryctes[i]} y Chrysochloris es {linaje_Chryso[i]}.")
        break
else:
    print(f"\nNotoryctes typhlops y Chrysochloris asiatica comparten el mismo linaje hasta {linaje_Notoryctes[-1]}.")

handle.close()

'''




