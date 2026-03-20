import os
import glob
import re
import shutil
from Cocoa import NSURL
from Quartz import PDFDocument

# --- Configurações da Mesa de Operação ---
STAGING_BASE = '04_PESQUISA_ANDAMENTO/CLEAN_ROOM_STAGING'
ORIGENS = [
    '01_GOVERNANCA',
    '02_TECNICO',
    '99_RESTRITO'
]

# Padrões de Expurgo
REPLACEMENTS = {
    r'\bPAR 5\.1\b': 'Protocolo Institucional v1.0',
    r'\bMestre 5\.2\b': '',
    r'(?i)Fabio Takwara': 'Coordenação Técnica',
    r'(?i)Takwara': 'Institucional' 
}

# Extensões Permitidas (Sem PDFs originais)
ALLOWED_EXT = ['.md', '.txt', '.py', '.yml', '.yaml', '.json']
IMAGE_EXT = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.pdf'] # PDF aqui apenas se for imagem técnica? Não, usuário disse "ignorar os originais (PDF)" para transcrição.

def purge_content(text):
    for pattern, sub in REPLACEMENTS.items():
        text = re.sub(pattern, sub, text)
    return text

def transcribe_pdf(pdf_path, txt_path):
    try:
        url = NSURL.fileURLWithPath_(os.path.abspath(pdf_path))
        doc = PDFDocument.alloc().initWithURL_(url)
        texto = doc.string() if doc else ''
        if texto and len(texto.strip()) > 50:
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(purge_content(texto))
            return True
    except Exception as e:
        print(f"❌ Erro PDF {pdf_path}: {e}")
    return False

def run_surgery():
    print("🚀 Iniciando Cirurgia de Realinhamento...")
    os.makedirs(STAGING_BASE, exist_ok=True)
    
    for raiz in ORIGENS:
        for root, dirs, files in os.walk(raiz):
            # Ignorar pastas de legado e a própria pasta de destino (EVITAR RECURSÃO)
            if any(x in root for x in ['07_BLOG_MEDIUM', 'QUARENTENA', 'dist_zenodo_v2.2.2', 'CLEAN_ROOM_STAGING']):
                continue
                
            for file in files:
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, '.')
                ext = os.path.splitext(file)[1].lower()
                
                # Destino sugerido mantendo estrutura
                dest_path = os.path.join(STAGING_BASE, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                if ext in ALLOWED_EXT:
                    # Ler, expurgar e salvar
                    try:
                        with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                        with open(dest_path, 'w', encoding='utf-8') as f:
                            f.write(purge_content(content))
                        print(f"✅ Processado: {rel_path}")
                    except Exception as e:
                        print(f"⚠️ Erro no arquivo {src_path}: {e}")
                
                elif ext == '.pdf':
                    # Transcrever se for da Sombra/Projeto
                    txt_dest = dest_path.replace('.pdf', '.txt')
                    if transcribe_pdf(src_path, txt_dest):
                        print(f"📄 Transcrito: {rel_path}")
                    else:
                        print(f"🚫 Ignorado/Imagem: {rel_path}")
                
                elif ext in ['.png', '.jpg', '.jpeg', '.svg']:
                    # Copiar imagens integralmente
                    shutil.copy2(src_path, dest_path)
                    print(f"🖼️ Imagem Copiada: {rel_path}")

    print("\n✨ Cirurgia Finalizada. Ativos realinhados em CLEAN_ROOM_STAGING.")

if __name__ == "__main__":
    run_surgery()
