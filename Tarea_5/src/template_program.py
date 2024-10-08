'''
NAME
        Tarea 5

VERSION
        1

AUTHOR
        Carlos García González

DESCRIPTION
         Este script de Python tiene dos funciones, utilizando las bibliotecas
         de "Biopython" y el módulo "Entrez" para interactuar con la base de 
         datos "Protein" del NCBI. La primera función realiza una búsqueda para
         encontrar proteínas relacionadas al gen DEFA en el mosquiro Aedes aegypti
         e imprime en pantalla los IDs que coinciden con el término de la búsqueda.

         La segunda función selecciona el primer ID y realiza una búsqueda en 
         "GeneBank" e imprime información detallada acerca de esta.



CATEGORY
        

USAGE

    python template_program
    

ARGUMENTS


METHOD
    Biopython/Tarea_5

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

# Configuracion del correo electronico para Entrez (requerido por NCBI)
Entrez.email = "carlosgg@lcg.unam.mx"

# Buscar en la base de datos de proteinas (protein) usando el termino DEFA y Aedes aegypti
handle = Entrez.esearch(db = "protein", term = "DEFA[Aedes aegypti]")
record = Entrez.read(handle)

print("Lista de Id's la informacion del gen DEFA del mosquito en la db de protein: ")
print(record["IdList"])

# Obtengo el ID de la primera proteina en los resultados de busqueda
prot_id = record["IdList"][0]

# Extraer el registro GenBank de la base de datos de proteinas usando el ID obtenido
handle = Entrez.efetch(db = "protein", id = prot_id, rettype = "gb", retmode = "text")
genbank_record = handle.read()
handle.close()

# Mostrar la informacion obtenida (o guardarla para analisis posterior)
print(genbank_record)
