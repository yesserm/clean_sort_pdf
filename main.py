import argparse
import re

import utils


def main():
    parser = argparse.ArgumentParser(description="PDF Extractor Tool")
    parser.add_argument('-i', '--input', required=True, help="Path to the input PDF file")
    parser.add_argument('-o', '--output', required=False, help="Path to the output file")
    parser.add_argument('-t', '--text', required=True, help="Text for filtering pages (e.g., '3 of' or 'benefits')")
    parser.add_argument('-r', '--reset', required=False, help="Text for resetting the filter (e.g., '1 of')")

    print("""
        █ Clean Sort PDF - Versión 1.0 █
    """)

    args = parser.parse_args()
    ruta_entrada = args.input
    ruta_salida = args.output if args.output else "samples\\output.pdf"
    texto_filtro = args.text if args.text else "3 of"
    reinicio_filtro = args.reset if args.reset else "1 of"

    print(f"Procesando el archivo: {ruta_entrada}")

    indices_paginas = utils.detectar_paginas_desde_filtro_reinicio(ruta_entrada, texto_filtro, reinicio_filtro)
    if indices_paginas:
        utils.crear_pdf_filtrado(ruta_entrada, indices_paginas, ruta_salida)
        print(f"PDF creado en {ruta_salida} con {len(indices_paginas)} páginas.")
    else:
        print(f"No se encontraron páginas con el texto '{texto_filtro}'.")


if __name__ == "__main__":
    main()