import os, glob, PyPDF2
from docling.document_converter import DocumentConverter

# --- Configurações Institucionais (WTF) ---
SOURCE_DIR = "99_RESTRITO/02_TRIAGEM_BRUTA"
DEST_DIR = "04_PESQUISA_ANDAMENTO/SONDA_DOCLING"

FILTRO_INSTITUCIONAL = [
    "bambu", "bamboo", "guadua", "timber", "bio-based", "biopolimero", "biopolymer", 
    "polyurethane", "poliuretano", "castor oil", "mamona", "amazonia", 
    "amazon", "regenerative", "bioeconomy", "geodesic", "geodesica", "dome",
    "mulheres", "feminina", "consorcio", "unb", "report", "relatorio", "article"
]

def avaliar_pdf(caminho):
    try:
        with open(caminho, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            texto = reader.pages[0].extract_text().lower()
            return any(termo in texto for termo in FILTRO_INSTITUCIONAL)
    except: return False

def disparar_sonda_institucional():
    converter = DocumentConverter()
    pdfs = glob.glob(os.path.join(SOURCE_DIR, "**/*.pdf"), recursive=True)
    os.makedirs(DEST_DIR, exist_ok=True)
    
    inventario_path = os.path.join(DEST_DIR, "00_INVENTARIO_CURADORIA_WTF.md")
    
    print(f"📡 Iniciando Mapeamento Institucional (Sonda WTF): {len(pdfs)} arquivos.")

    with open(inventario_path, "a", encoding="utf-8") as f_inv:
        f_inv.write(f"# 🗂️ Inventário de Curadoria - Mulheres Que Tecem a Floresta\n\n")

        for path in pdfs:
            if avaliar_pdf(path):
                nome = os.path.basename(path)
                print(f"📍 Localizado: {nome}")
                try:
                    result = converter.convert(path)
                    resumo_curto = result.document.export_to_markdown()[:500]
                    
                    f_inv.write(f"## 📄 {nome}\n")
                    f_inv.write(f"- **📍 Localização:** `{path}`\n")
                    f_inv.write(f"- **🔍 Prévia do Conteúdo:** {resumo_curto}...\n")
                    f_inv.write(f"- **⚠️ Status:** Requer análise BNDES/Model-01\n")
                    f_inv.write(f"---\n\n")
                    
                    print(f"✅ Indexado: {nome}")
                except Exception as e:
                    f_inv.write(f"## 📄 {nome} (ERRO NA INDEXAÇÃO)\n")
                    f_inv.write(f"- **📍 Localização:** `{path}`\n")
                    f_inv.write(f"- **❌ Erro:** {str(e)[:100]}\n---\n\n")

if __name__ == "__main__":
    disparar_sonda_institucional()
