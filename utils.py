import pdfplumber
from PyPDF3 import PdfFileReader, PdfFileWriter
    
def detectar_paginas_desde_filtro(ruta_pdf, texto_clave, min_chars=100): 
    """ Devuelve índices de páginas desde la primera que contiene el texto_clave hasta el final del documento, excluyendo las páginas con menos de min_chars caracteres. """ 
    indices = [] 
    start_index = None 
    with pdfplumber.open(ruta_pdf) as pdf: 
        for i, pagina in enumerate(pdf.pages): 
            contenido = pagina.extract_text() 
            if contenido and contenido.strip(): 
                if texto_clave in contenido: 
                    start_index = i 
                    break 
        
        if start_index is not None: 
            for i in range(start_index, len(pdf.pages)): 
                contenido = pdf.pages[i].extract_text() 
                if contenido and len(contenido.strip()) >= min_chars: 
                    indices.append(i)
    return indices

def detectar_paginas_desde_filtro_reinicio(ruta_pdf, texto_clave = "3 of", reinicio_clave = "1 of", min_chars=100): 
    """ Devuelve índices de páginas desde la primera que contiene el texto_clave hasta el final del documento, excluyendo las páginas con menos de min_chars caracteres. """ 
    indices = [] 
    start_index = None 
    with pdfplumber.open(ruta_pdf) as pdf: 
        for i, pagina in enumerate(pdf.pages): 
            contenido = pagina.extract_text() 
            if contenido and contenido.strip(): 
                if texto_clave in contenido: 
                    start_index = i 
                    break 
        
        if start_index is not None: 
            for i in range(start_index, len(pdf.pages)): 
                contenido = pdf.pages[i].extract_text() 
                if contenido and contenido.strip(): 
                    if reinicio_clave in contenido: 
                        stop_index = i 
                        break 
                    if len(contenido.strip()) >= min_chars: 
                        indices.append(i)
    return indices

def crear_pdf_filtrado(ruta_pdf, indices, ruta_salida): 
    """Crea un nuevo PDF con las páginas seleccionadas.""" 
    reader = PdfFileReader(open(ruta_pdf, "rb")) 
    writer = PdfFileWriter() 
    for i in indices: 
        writer.addPage(reader.getPage(i)) 
    with open(ruta_salida, "wb") as salida: 
        writer.write(salida)

