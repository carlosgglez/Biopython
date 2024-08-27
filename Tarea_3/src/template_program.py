'''
NAME
        Tarea 3

VERSION
        1

AUTHOR
        Carlos García González

DESCRIPTION
        Este script de Python utiliza la biblioteca Biopython y el módulo
        Entrez para interactuar con la base de datos “Taxonomy" del NCBI. 
        Recopila datos taxonómicos de dos organismos usando sus IDs 
        correspondientes, y divide la información del linaje en una lista 
        de categorías taxonómicas para su posterior comparación. Es útil 
        para comparar la taxonomía de dos organismos y determinar el punto 
        exacto en el que sus linajes divergen.


CATEGORY
        

USAGE

    python template_program
    

ARGUMENTS


METHOD
    Biopython/Tarea_3

SEE ALSO


        
'''


# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez
from pprint import pprint  # Mejor visualización de diccionarios


# ===========================================================================
# =                            main
# ===========================================================================

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
