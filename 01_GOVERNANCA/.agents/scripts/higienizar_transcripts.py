import os, glob, re

TXT_DIR = '04_PESQUISA_ANDAMENTO/TRANSCRIPT'

def limpar_texto(texto):
    # 1. Corrige caracteres acentuados comuns de erro de PDF
    correcoes = {'Ã³': 'ó', 'Ã£': 'ã', 'Ã©': 'é', 'Ã¡': 'á', 'Ã§': 'ç', 'Ãª': 'ê', 'Ã': 'í'}
    for erro, acerto in correcoes.items():
        texto = texto.replace(erro, acerto)
    
    # 2. Remove números de página isolados (ex: \n 12 \n)
    texto = re.sub(r'\n\s*\d+\s*\n', '\n', texto)
    
    # 3. Une palavras hifenizadas no final da linha (ex: bio-\neconomia)
    texto = re.sub(r'(\w+)-\n(\w+)', r'\1\2', texto)
    
    return texto

for path in glob.glob(f'{TXT_DIR}/*.txt'):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        conteudo = f.read()
    
    conteudo_limpo = limpar_texto(conteudo)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(conteudo_limpo)
    print(f"🧹 Higienizado: {os.path.basename(path)}")