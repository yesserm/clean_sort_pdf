import argparse

import utils

def main():
    parser = argparse.ArgumentParser(description="PDF Extractor Tool")
    parser.add_argument('-i', '--input', required=True, help="Path to the input PDF file")
    parser.add_argument('-o', '--output', required=False, help="Path to the output file")
    parser.add_argument('-p', '--pages', required=False, help="Pages to extract (e.g., 1,2,3 or 1-3)")
    parser.add_argument('-t', '--text', required=True, help="Text for filtering pages (e.g., '3 de 3' or 'Alternativa')")
    
    print("""
        █ Clean Sort PDF - Versión 1.0 █
    """)  

    args = parser.parse_args()
    if args.input:
        ruta_entrada = args.input if args.input else "input.pdf"
        ruta_salida = args.output if args.output else "output.pdf" 
        texto_filtro = args.text if args.text else "3 de 3"
        
        reader = utils.leer_pdf(ruta_entrada) 
        paginas_seleccionadas = [] 

        for i in range(reader.getNumPages()): 
            pagina = reader.getPage(i) 
            if utils.es_pagina_vacia(pagina): 
                continue 
            if utils.contiene_texto(pagina, texto_filtro): 
                paginas_seleccionadas.append(pagina) 
                if paginas_seleccionadas: 
                    utils.crear_pdf(paginas_seleccionadas, ruta_salida) 
                    print(f"PDF creado en {ruta_salida} con {len(paginas_seleccionadas)} páginas.") 
                else: 
                    print(f"No se encontraron páginas con el texto '{texto_filtro}'.")  

if __name__ == "__main__":
    main()