# --- EXPLICAÇÃO DIDÁTICA PARA FABIO ---
# O QUE FAZ: Este é o seu "Recuperador de Documentos". Ele usa OCR para ler PDFs 
# que são apenas imagens (escaneados) e extrair o texto.
# 
# POR QUE É NECESSÁRIO: Muitos testes do ITecons chegam como imagens protegidas.

import os
from pdf2image import convert_from_path
import pytesseract

def executar_ocr(caminho_pdf, saida_md):
    print(f"⏳ OCR em: {caminho_pdf}")
    paginas = convert_from_path(caminho_pdf, 300)
    texto = ""
    for pag in paginas:
        texto += pytesseract.image_to_string(pag, lang='por') + "\n---\n"
    with open(saida_md, "w") as f: f.write(texto)
    print(f"✅ Texto extraído para: {saida_md}")

if __name__ == "__main__":
    # Exemplo de uso
    pass
