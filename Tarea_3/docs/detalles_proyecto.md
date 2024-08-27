# Busqueda y Comparacion de linajes

Fecha: 26/08/2024

**Participantes:** Carlos Garcia Gonzales  <email: carlosgg@lcg.unam.mx>


## Descripción del problema: 
Al analizar dos organismos, es crucial tener una eficacia en nuestro trabajo, pero también una exactitud que no podríamos lograr manualmente, por lo que este script tiene como finalidad la entrega de nuestro trabajo en base de esos dos criterios, eficacia y exactitud. Para poder descubrir la divergencia entre ambos.

## Especificación de Requisitos: 

Requisitos no funcionales. 

- El script debe estar escrito en Python
- El tiempo de consulta, sin importar su dimensión, debe ser rápido.

## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

'''
from Bio import Entrez
from pprint import pprint  # Mejor visualización de diccionarios

Entrez.email = "carlosgg@lcg.unam.mx"

handle = Entrez.esearch(db="Taxonomy", term="Notoryctes typhlops")
record = Entrez.read(handle)
print("El Id de Notoryctes typhlops es: ")
print(record["IdList"])

Id_Notoryctes = record["IdList"]
handle = Entrez.efetch(db="Taxonomy", id=Id_Notoryctes, retmode="xml")
Notoryctes = Entrez.read(handle)

handle = Entrez.esearch(db="Taxonomy", term="Chrysochloris asiatica")
record = Entrez.read(handle)
print(f"\nEl Id de Chrysochloris asiatica es: ")
print(record["IdList"])

Id_Chryso = record["IdList"]
handle = Entrez.efetch(db="Taxonomy", id=Id_Chryso, retmode="xml")
Chryso = Entrez.read(handle)

print(f"\nLinaje de Notoryctes typhlops:")
linaje_Notoryctes = Notoryctes[0]["Lineage"].split("; ")
print(" > ".join(linaje_Notoryctes))

print(f"\nLinaje de Chrysochloris asiatica:")
linaje_Chryso = Chryso[0]["Lineage"].split("; ")
print(" > ".join(linaje_Chryso))

for i in range(min(len(linaje_Notoryctes), len(linaje_Chryso))):
    if linaje_Notoryctes[i] != linaje_Chryso[i]:
        print(f"\nLos linajes de Notoryctes typhlops y Chrysochloris asiatica divergen después de ser ambos {linaje_Notoryctes[i-1]}.")
        print(f"Notoryctes es {linaje_Notoryctes[i]} y Chrysochloris es {linaje_Chryso[i]}.")
        break
else:
    print(f"\nNotoryctes typhlops y Chrysochloris asiatica comparten el mismo linaje hasta {linaje_Notoryctes[-1]}.")

handle.close()

'''
