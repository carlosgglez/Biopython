# E.search

Fecha: 10/08/2024

**Participantes**
Carlos García González <email: carlosgg@lcg.unam.mx>


## Descripción del Problema

El problema principal a resolver es realizar una búsqueda avanzada con etiquetas específicas, para después generar un archivo a partir de segmentos de dichos datos y ese archivo que realice un búsqueda inversa de citas que se le hayan realizado a los datos.

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
termino = "(Auvynet-C[AUTH]) AND ((peptide[TITLE] OR peptides[TITLE]) OR (antimicrobial[TITLE] OR migration[TITLE]))"



try:
    handle = Entrez.esearch(db="pubmed", term=termino, retmax=100)
    record = Entrez.read(handle)
    handle.close()  # Cierra el handle de la busqueda

    print("IDs de los articulos encontrados:")
    pprint(record["IdList"])  # Se usa pprint para una mejor visualizacion

    Id_Constance = record["IdList"]

    if not Id_Constance:
        print("No se encontraron articulos.")
    else:
       
        handle = Entrez.efetch(db="pubmed", id=Id_Constance, rettype="abstract", retmode="text")
        abstracts = handle.read()
        handle.close()  # Cierra el handle de la consulta

        filename_abstracts = "Abstracts_Constance_Auvynet.md"

        try:
            with open(filename_abstracts, "w", encoding="utf-8") as file:
                file.write(abstracts)
            print(f"Abstracts guardados en {filename_abstracts}")
        except IOError as e:
            print(f"Error al guardar el archivo: {e}")
            
        all_citations = []

        for pubmed_id in Id_Constance:
            handle = Entrez.elink(dbfrom="pubmed", id=pubmed_id, linkname="pubmed_pubmed_citedin")
            citation_record = Entrez.read(handle)
            handle.close()

            if citation_record[0]["LinkSetDb"]:
                citation_ids = [link["Id"] for link in citation_record[0]["LinkSetDb"][0]["Link"]]
                all_citations.extend(citation_ids)

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

'''




