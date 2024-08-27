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
        
        La otra función que tiene el prgrama es de buscar en la base de 
        datos de Pubmed las entradas que hay de la Doctora Constance Auvynet,
        especificando encontrar los artículos que en el titulo mencionen algo
        sobre "peptide", "antimicrobial" o "migration".


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

from Bio import Entrez
from pprint import pprint

# Configuracion del correo electronico para Entrez (requerido por NCBI)
Entrez.email = "carlosgg@lcg.unam.mx"

# Define el termino de busqueda para PubMed, buscando articulos de un autor especifico con palabras clave en el titulo
termino = "(Auvynet-C[AUTH]) AND ((peptide[TITLE] OR peptides[TITLE]) OR (antimicrobial[TITLE] OR migration[TITLE]))"

try:
    # Realiza la busqueda en PubMed con el termino especificado
    handle = Entrez.esearch(db="pubmed", term=termino, retmax=100)
    record = Entrez.read(handle)
    handle.close()  # Cierra el handle de la busqueda

    print("IDs de los articulos encontrados:")
    pprint(record["IdList"])  # Se usa pprint para una mejor visualizacion

    Id_Constance = record["IdList"]

    if not Id_Constance:
        print("No se encontraron articulos.")
    else:
        # Obtener los abstracts de los articulos encontrados
        handle = Entrez.efetch(db="pubmed", id=Id_Constance, rettype="abstract", retmode="text")
        abstracts = handle.read()
        handle.close()  # Cierra el handle de la consulta

        # Define el nombre del archivo donde se guardaran los abstracts de los articulos
        filename_abstracts = "Abstracts_Constance_Auvynet.md"

        # Guarda los abstracts en el archivo usando utf-8 para manejar caracteres Unicode
        try:
            with open(filename_abstracts, "w", encoding="utf-8") as file:
                file.write(abstracts)
            print(f"Abstracts guardados en {filename_abstracts}")
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")

        # Obtener los IDs de los articulos que citan a los articulos encontrados
        all_citations = []

        for pubmed_id in Id_Constance:
            handle = Entrez.elink(dbfrom="pubmed", id=pubmed_id, linkname="pubmed_pubmed_citedin")
            citation_record = Entrez.read(handle)
            handle.close()

            # Extraer los IDs de los articulos citantes
            if citation_record[0]["LinkSetDb"]:
                citation_ids = [link["Id"] for link in citation_record[0]["LinkSetDb"][0]["Link"]]
                all_citations.extend(citation_ids)

        # Guardar los IDs de las citas en un archivo
        filename_citations = "Citations_Constance_Auvynet.txt"
        try:
            with open(filename_citations, "w", encoding="utf-8") as file:
                for citation_id in all_citations:
                    file.write(citation_id + "\n")
            print(f"IDs de los articulos citantes guardados en {filename_citations}")
        except IOError as e:
            print(f"Error al guardar el archivo de citas: {e}")

except Exception as e:
    print(f"Se produjo un error: {e}")
