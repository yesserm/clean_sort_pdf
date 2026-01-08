import pdfplumber
from PyPDF3 import PdfFileReader, PdfFileWriter

def detectar_paginas(ruta_pdf, texto_clave): 
    """Devuelve índices de páginas que contienen el texto clave y no están vacías.""" 
    indices = [] 
    with pdfplumber.open(ruta_pdf) as pdf: 
        for i, pagina in enumerate(pdf.pages): 
            contenido = pagina.extract_text()
            if contenido and contenido.strip(): 
                if texto_clave in contenido: 
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