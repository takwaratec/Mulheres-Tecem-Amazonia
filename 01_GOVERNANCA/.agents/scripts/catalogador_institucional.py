import os, glob
try:
    from Cocoa import NSURL
    from Quartz import PDFDocument
except ImportError:
    print('❌ Erro: Execute primeiro: pip3 install pyobjc-framework-Cocoa pyobjc-framework-Quartz')
    exit()

# Novos caminhos institucionais (WTF)
origens = [
    '99_RESTRITO/02_TRIAGEM_BRUTA/03_COLABORADORES'
]

destino = '04_PESQUISA_ANDAMENTO/TRANSCRIPT/BIOECONOMIA_FEMININA'
os.makedirs(destino, exist_ok=True)

print(f'🚀 Iniciando Coleta Institucional (Mulheres-Tecem)...')

for raiz in origens:
    arquivos = glob.glob(os.path.join(raiz, '**/*.pdf'), recursive=True)
    for p in arquivos:
        nome_base = os.path.basename(p).replace(' ', '_')
        txt_saida = os.path.join(destino, f'RAW_{nome_base}.txt')
        
        if os.path.exists(txt_saida): continue

        url = NSURL.fileURLWithPath_(os.path.abspath(p))
        doc = PDFDocument.alloc().initWithURL_(url)
        texto = doc.string() if doc else ''
        
        if texto and len(texto.strip()) > 50:
            with open(txt_saida, 'w', encoding='utf-8') as f:
                f.write(texto)
            print(f'✅ Transcrito: {nome_base}')
        else:
            print(f'⚠️  Imagem/Vazio: {nome_base}')

print(f'\n✨ Processo finalizado. Verifique a pasta {destino}')
