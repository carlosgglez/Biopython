'''
NAME
        Tarea 1

VERSION
        1

AUTHOR
        Carlos García González

DESCRIPTION
        Este script de Python utiliza las bibliotecas de "Biopython" y de
        "Entrez" para hacer una consulta en la base de datos de "Pubmed", 
        regresando la siguiente información de todos los FieldList:
            - Name
            - Full Name
            - Description
        
        De igual manera, regresa la descripción del primer FieldList

CATEGORY
        

USAGE

    python template_program
    

ARGUMENTS


METHOD
    Biopython/Tarea_1

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

Entrez.email = "carlosgg@lcg.unam.mx"

handle = Entrez.einfo(db="pubmed")
record = Entrez.read(handle)

# 1. Iterar sobre todos los campos en FieldList e imprimir nombre, FullName y descripción
for field in record["DbInfo"]["FieldList"]:
    print(field["Name"] + "," + field["FullName"] + "," + field["Description"])

# Imprimir la URL de la consulta
print("\nURL de la consulta:", handle.url)

# 2. Imprimir la descripción del primer campo
primer_campo = record['DbInfo']['FieldList'][0]
print("\nDescripción del primer campo:")
print(primer_campo["Description"])

# Cerrar el handle después de obtener toda la información
handle.close()

