from PyPDF3 import PdfFileReader, PdfFileWriter, PdfMerger

def leer_pdf(ruta_pdf):
    """Devuelve un objeto PdfFileReader para el PDF dado."""
    return PdfFileReader(open(ruta_pdf, 'rb'))

def fusionar_pdfs(rutas_pdfs, ruta_salida):
    """Fusiona varios PDFs en uno solo."""
    merger = PdfMerger()
    for ruta in rutas_pdfs:
        merger.append(ruta)
    merger.write(ruta_salida)
    merger.close()

def contiene_texto(pagina, texto):
    """Verifica si la página contiene el texto buscado."""
    contenido = pagina.extractText()
    return contenido and texto in contenido

def es_pagina_vacia(pagina):
    """Devuelve True si la página está vacía o sin texto útil."""
    contenido = pagina.extractText()
    return not contenido or not contenido.strip()

def filtrar_paginas(reader, criterio):
    """Devuelve las páginas que cumplen el criterio."""
    paginas_filtradas = []
    for i in range(reader.getNumPages()):
        pagina = reader.getPage(i)
        if criterio(pagina):
            paginas_filtradas.append(pagina)
    return paginas_filtradas

def crear_pdf(paginas, ruta_salida):
    """Crea un nuevo PDF con las páginas seleccionadas."""
    escritor = PdfFileWriter()
    for pagina in paginas:
        escritor.addPage(pagina)
    with open(ruta_salida, 'wb') as archivo_salida:
        escritor.write(archivo_salida)