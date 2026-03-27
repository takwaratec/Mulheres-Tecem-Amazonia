import os
from pdf2image import convert_from_path
import pytesseract
from PIL import Image

# --- CONFIGURAÇÃO DE CAMINHOS ---
# O arquivo que veio vazio no Docling
PDF_ENTRADA = "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Tecnoveg/QUI1385-25 resistência química.pdf"
# Onde vamos salvar o texto recuperado
MD_SAIDA = "99_RESTRITO/02_TRIAGEM_BRUTA/WA_MAM/Tecnoveg/Tecnoveg-markdown/LAUDO_COMPATIBILIDADE_TECNICA.md"

def executar_ocr_recuperacao():
    print(f"⏳ Iniciando OCR de imagem no arquivo: {PDF_ENTRADA}")
    
    if not os.path.exists(PDF_ENTRADA):
        print("❌ Arquivo PDF não encontrado!")
        return

    try:
        # 1. Converte as páginas do PDF em imagens de alta resolução (300 DPI)
        print("📸 Convertendo páginas do PDF em imagens...")
        paginas = convert_from_path(PDF_ENTRADA, 300)
        
        texto_completo = []
        
        # 2. Varre cada página extraindo o texto
        for i, pagina_img in enumerate(paginas):
            print(f"🔍 Lendo página {i+1} de {len(paginas)}...")
            
            # pytesseract lê a imagem e busca texto em português
            texto_da_pagina = pytesseract.image_to_string(pagina_img, lang='por')
            
            texto_completo.append(f"## CONTEÚDO RECUPERADO - PÁGINA {i+1}\n")
            texto_completo.append(texto_da_pagina)
            texto_completo.append("\n---\n")

        # 3. Salva o resultado no formato Markdown
        with open(MD_SAIDA, "w", encoding="utf-8") as f:
            f.write("\n".join(texto_completo))
            
        print(f"✅ SUCESSO! O texto foi extraído e salvo em: {MD_SAIDA}")
        print("💡 Agora você pode rodar o 'gerador_review_tecnoveg.py' sobre este novo arquivo.")

    except Exception as e:
        print(f"❌ Ocorreu um erro durante o OCR: {e}")

if __name__ == "__main__":
    executar_ocr_recuperacao()


# python ocr_laudo_tecnoveg.py