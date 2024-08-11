'''
NAME
        Tarea 2

VERSION
        1

AUTHOR
        Carlos García González

DESCRIPTION
        Este script de Python utiliza las bibliotecas de "Biopython" y de
        "Entrez" para hacer una consulta en la base de datos de "Protein", 
        regresando la descripción del FieldList "ECNO" y la descripción del
        LinklList "protein_protein_small_genome".

CATEGORY
        

USAGE

    python template_program
    

ARGUMENTS


METHOD
    Biopython/Tarea_2

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

# Configuración del correo electrónico para Entrez (requerido por NCBI)
Entrez.email = "carlosgg@lcg.unam.mx"

# Consulta la base de datos "protein" para obtener información sobre los campos
handle = Entrez.einfo(db="protein")
record = Entrez.read(handle)

# Obtiene la descripción del campo ECNO desde la lista de campos
ECNO_campo = record['DbInfo']['FieldList'][16]
print("\nDescripción del campo ECNO:")
print(ECNO_campo["Description"])

# Imprime la URL de la consulta realizada a Entrez
print("\nURL de la consulta:", handle.url)

# Obtiene la descripción del campo protein_protein_small_genome desde la lista de enlaces
protein_campo = record['DbInfo']['LinkList'][33]
print("\nDescripción del campo protein_protein_small_genome:")
print(protein_campo["Description"])

# Define el nombre del archivo donde se guardarán los IDs de los artículos
filename = "Id's_Constance_Auvynet.md"

# Define el término de búsqueda para PubMed, buscando artículos de un autor específico con palabras clave en el título
termino = "(Auvynet-C[AUTH]) AND ((peptide[TITLE] OR peptides[TITLE]) OR (antimicrobial[TITLE] OR migration[TITLE]))"

# Realiza la búsqueda en PubMed con el término especificado
handle = Entrez.esearch(db="pubmed", term=termino, retmax=100)
record = Entrez.read(handle)

# Define el nombre del archivo de salida y guarda los IDs de los artículos encontrados
archivo_salida = "Ids_Constance_Auvynet.md"
with open(archivo_salida, "w") as file:
    file.write("\n".join(record["IdList"]))

# Imprime la confirmación de que los IDs se han guardado en el archivo
print(f"\nIDs guardados en {archivo_salida}")

# Cierra el handle de la consulta para liberar recursos
handle.close()
