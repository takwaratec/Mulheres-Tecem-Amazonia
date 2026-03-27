from docling.document_converter import DocumentConverter
import os

# 1. Coordenadas
ENTRADA = "/Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia/PESQUISA_GRAFISMO/PESQUISA_GRAFISMO/CATALOGO_GRAFISMOS_REMOTO"
SAIDA = "DOCLING_PDF-MD"
os.makedirs(SAIDA, exist_ok=True)

def extrair_com_docling():
    converter = DocumentConverter()
    
    # Busca os PDFs baixados pelo seu Agente
    arquivos = [f for f in os.listdir(ENTRADA) if f.endswith(".pdf")]
    
    for arquivo in arquivos:
        print(f"🧬 Mapeando estrutura de: {arquivo}...")
        caminho_pdf = os.path.join(ENTRADA, arquivo)
        
        # O Docling faz a mágica: entende o que é tabela e o que é imagem
        result = converter.convert(caminho_pdf)
        
        # Exporta como Markdown (Preserva a estrutura visual da tabela)
        nome_base = os.path.splitext(arquivo)[0]
        caminho_md = os.path.join(SAIDA, f"{nome_base}.md")
        
        with open(caminho_md, "w", encoding="utf-8") as f:
            f.write(result.document.export_to_markdown())
            
    print(f"✅ Tabelas exportadas com sucesso em: {SAIDA}")

if __name__ == "__main__":
    extrair_com_docling()


# python extrator_docling.py