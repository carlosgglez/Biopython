# Buscar el accesion de UniProt

Fecha: 08/09/2024

**Participantes**
Carlos García González <email: carlosgg@lcg.unam.mx>


## Descripción del Problema

Este script de Python tiene dos funciones, utilizando la biblioteca
de "Biopython" y los módulos "SeqIO", "NCBIWWW" y "NCBIXML" para interactuar
con la base de datos "nr" del NCBI. La primera función carga un archivo fasta 
que contiene una única secuencia, después realiza una busqueda BLAST en la base 
de datos nr y por último filtra y muestra alineamientos cuyo valor E es menor que 0.05.

La segunda función también carga un archivo fasta, pero este, a diferencia del primero,
contiene multiples secuencias, para cada secuencia, realiza una búsqueda BLAST y encuentra
el alineamiento con el mejor score y cuyo valor E sea menor que 0.05.
Si encuentra un alineamiento significativo, imprime sus detalles. Si no, informa que no hay
alineamientos con un valor E dentro del umbral.

## Especificación de Requisitos

Requisitos no funcionales

- El script debe de estar escrito en Python
- El tiempo de respuesta debe de ser rápido, incluso si se hace una consulta grande


## Análisis y Diseño

Para resolver este problema, se utilizarán varias funciones incorporadas en Python. A continuación, se muestra un pseudocódigo simple para ilustrar la lógica básica del script:

'''
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from pprint import pprint  # Mejor visualización de diccionarios

input_file_1 = "opuntia1.fasta"

record = SeqIO.read(input_file_1, format="fasta")

result_handle = NCBIWWW.qblast("blastn", "nr", record.seq, format_type="XML")

blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.05

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            print("Sequence Title:", alignment.title)
            print("Length:", alignment.length)
            print("E-value:", hsp.expect)
            print()

print("Búsqueda completada para opuntia1.fasta.\n")

input_file_2 = "opuntia.fasta"

sequences = SeqIO.parse(input_file_2, format="fasta")

for seq_record in sequences:
    print(f"Procesando secuencia: {seq_record.id}")

    
    result_handle = NCBIWWW.qblast("blastn", "nr", seq_record.seq, format_type="XML")
    

    blast_record = NCBIXML.read(result_handle)
    

    best_alignment = None
    best_hsp = None

    
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                if best_hsp is None or hsp.score > best_hsp.score:
                    best_alignment = alignment
                    best_hsp = hsp
    
    
    if best_alignment and best_hsp:
        print("****Mejor Alineamiento****")
        print("Sequence Title:", best_alignment.title)
        print("Length:", best_alignment.length)
        print("E-value:", best_hsp.expect)
        print("Score:", best_hsp.score)
        print()
    else:
        print("No se encontraron alineamientos significativos con p-value < 0.05.\n")

print("Búsqueda completada para opuntia.fasta.")
'''




