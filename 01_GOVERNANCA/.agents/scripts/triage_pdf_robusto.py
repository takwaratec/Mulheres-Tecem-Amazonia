#!/usr/bin/env python3
import os
import subprocess
import glob
import sys

# Tente importar as bibliotecas macOS nativas, se falhar, use uma alternativa ou avise o usuário
try:
    from Cocoa import NSURL
    from Quartz import PDFDocument
except ImportError:
    print("⚠️ Bibliotecas PyObjC (Cocoa/Quartz) não encontradas. Instale com: pip install pyobjc-framework-Quartz")
    sys.exit(1)

# Configurações de Caminho (Relativas ao Repositório)
# O usuário pode passar os caminhos via argumento ou usar os padrões abaixo
PASTA_ORIGEM = sys.argv[1] if len(sys.argv) > 1 else "99_RESTRITO/02_TRIAGEM_BRUTA"
PASTA_DESTINO = sys.argv[2] if len(sys.argv) > 2 else "01_SOMBRA_AUDITORIA/01_TECNOLOGIA_TAKWARA"

def extrair_texto_nativo(caminho_pdf):
    try:
        url = NSURL.fileURLWithPath_(os.path.abspath(caminho_pdf))
        doc = PDFDocument.alloc().initWithURL_(url)
        return doc.string() if doc else ""
    except Exception as e:
        print(f"❌ Erro ao ler PDF: {e}")
        return ""

def pedir_ao_gemini(texto, nome_arquivo):
    # Prompt de Biblioteconomista Sênior (Padrão Takwara/WTF)
    prompt = f"""
    Aja como Biblioteconomista Sênior do Acervo Amazônia Regenerativa. 
    Analise este documento técnico: '{nome_arquivo}'.
    Gere um arquivo Markdown estruturado seguindo o Padrão Advocacy 5.1:
    
    1. Codificação: [Gerar sigla inteligente, ex: WTF-CAT-001 ou TAK-IMP-001]
    2. Área: [Categorize: Bioeconomia / Construção / Governança / etc]
    3. Resumo Técnico: (Exatamente 5 linhas focadas em aplicação prática e materiais)
    4. Ligação com Mulheres Bioeconomia Amazônia (WTF): (Como esta tecnologia ou dado empodera o projeto nos territórios AC-RR-AM?)
    5. Recomendação: [Mover para docs / Manter em sombra / Restrito]
    
    REGRAS: 
    - Sem saudações de IA.
    - Proibido mencionar venenos ou cimento.
    - Se houver menção a bioclean/pirolenhoso, destacar.
    
    Texto para análise (Amostra 8000 chars):
    {texto[:8000]} 
    """
    
    # Nota: Este script assume que o comando 'gemini' está no PATH do shell
    try:
        # Usamos uma string única para o comando para evitar problemas de escape no shell
        cmd = f"gemini '{prompt.replace(\"'\", \"'\\\\''\")}'"
        resultado = subprocess.run(['bash', '-c', cmd], capture_output=True, text=True)
        if resultado.returncode == 0:
            return resultado.stdout
        else:
            return f"❌ Erro no Gemini CLI: {resultado.stderr}"
    except Exception as e:
        return f"❌ Falha ao chamar Gemini: {e}"

def main():
    if not os.path.exists(PASTA_DESTINO):
        os.makedirs(PASTA_DESTINO, exist_ok=True)

    pdfs = glob.glob(os.path.join(PASTA_ORIGEM, "*.pdf"))
    print(f"🚀 Iniciando catalogação robusta de {len(pdfs)} arquivos...")

    for caminho in pdfs:
        nome_pdf = os.path.basename(caminho)
        print(f"📖 Processando: {nome_pdf}")
        
        conteudo = extrair_texto_nativo(caminho)
        if conteudo:
            analise = pedir_ao_gemini(conteudo, nome_pdf)
            nome_saida = nome_pdf.replace(".pdf", ".md")
            # Adicionamos o prefixo de catalogação inteligente
            caminho_saida = os.path.join(PASTA_DESTINO, f"CATALOGO_{nome_saida}")
            
            with open(caminho_saida, "w") as f:
                f.write(analise)
            print(f"✅ Catálogo gerado: {nome_saida}")
        else:
            print(f"⚠️ PDF sem texto extraível ou erro: {nome_pdf}")

    print(f"\n✨ Triagem concluída. Arquivos em: {PASTA_DESTINO}")

if __name__ == "__main__":
    main()
