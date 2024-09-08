'''
NAME
        Tarea 6

VERSION
        1

AUTHOR
        Carlos García González

DESCRIPTION
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



CATEGORY
        

USAGE

        python template_program
        
        Para poder correr este porgrama se necesita que tanto el programa, como los archivo
        "opuntia1.fasta" y "opuntia.fasta", se encuentren en el mismo directorio, puede
        ser en "Descargas", "Escritorio" o donde usted guste.
    

ARGUMENTS


METHOD
    Biopython/Tarea_6

SEE ALSO


        
'''


# ===========================================================================
# =                            imports
# ===========================================================================

from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from pprint import pprint  # Mejor visualización de diccionarios


# ===========================================================================
# =                            main
# ===========================================================================

# Especificar la ruta completa o relativa al archivo FASTA
input_file_1 = "opuntia1.fasta"

# Leer la secuencia en el archivo FASTA
record = SeqIO.read(input_file_1, format="fasta")

# Realizar la búsqueda BLAST en la base de datos 'nr'
result_handle = NCBIWWW.qblast("blastn", "nr", record.seq, format_type="XML")

# Parsear los resultados en formato XML
blast_record = NCBIXML.read(result_handle)

# Umbral para el valor E
E_VALUE_THRESH = 0.05

# Iterar sobre los alineamientos y filtrar por e-value
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            print("Sequence Title:", alignment.title)
            print("Length:", alignment.length)
            print("E-value:", hsp.expect)
            print()

print("Búsqueda completada para opuntia1.fasta.\n")

# Especificar la ruta completa o relativa al archivo FASTA
input_file_2 = "opuntia.fasta"

# Leer todas las secuencias en el archivo FASTA
sequences = SeqIO.parse(input_file_2, format="fasta")

# Procesar cada secuencia individualmente
for seq_record in sequences:
    print(f"Procesando secuencia: {seq_record.id}")
    
    # Realizar la búsqueda BLAST en la base de datos 'nr'
    result_handle = NCBIWWW.qblast("blastn", "nr", seq_record.seq, format_type="XML")
    
    # Parsear los resultados en formato XML
    blast_record = NCBIXML.read(result_handle)
    
    # Variables para guardar el mejor alineamiento
    best_alignment = None
    best_hsp = None
    
    # Iterar sobre los alineamientos y encontrar el de mayor score con e-value < 0.05
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                if best_hsp is None or hsp.score > best_hsp.score:
                    best_alignment = alignment
                    best_hsp = hsp
    
    # Si se encontró un alineamiento que cumple con el criterio, imprimir los detalles
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