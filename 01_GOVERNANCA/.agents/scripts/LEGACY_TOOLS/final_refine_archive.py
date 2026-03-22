import os
import re
from pathlib import Path

# Configuration
REPO_ROOT = Path("/Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia")
REVIEWS_DIR = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"
INDEX_PATH = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/03_METADATA_CATALOG/WTF_INDEX_ACERVO.md"

def refine_file(file_path):
    # Check size
    is_preview = file_path.stat().st_size < 2000
    print(f" Refining: {file_path.name} (is_preview={is_preview})")
    
    content = file_path.read_text(encoding="utf-8")
    
    # 1. Parse existing metadata to preserve project and equipment etc.
    metadata = {}
    header_raw = re.search(r"^---(.*?)---", content, re.DOTALL | re.MULTILINE)
    if header_raw:
        header_text = header_raw.group(1)
        for line in header_text.split('\n'):
            if ':' in line:
                k, v = line.split(':', 1)
                metadata[k.strip()] = v.strip()
                
    # 2. Extract Year from filename if possible
    year_match = re.search(r"\b(19|20)\d{2}\b", file_path.name)
    year = year_match.group(0) if year_match else metadata.get('data', '2025').replace("'", "")
    
    # 3. Clean filename to get a potential title/author
    clean_name = file_path.name.replace("WTF_RES_", "").replace(".pdf.md", "").replace(".md", "").replace("_", " ").title()

    # 4. Construct NEW HEADER
    new_header = "---"
    new_header += f"\nprojeto: Mulheres Que Tecem a Floresta"
    new_header += f"\ninstituicao: Consórcio UnB/UFAC/UFRR"
    new_header += f"\nequipe: {metadata.get('equipe', 'Gestão e Parceria Regional')}"
    new_header += f"\ntipo: {'Acervo de Pesquisa (Resenha Técnica)' if not is_preview else 'Acervo de Consulta (Ficha Técnica)'}"
    new_header += f"\nautor_original: Not Identified" # Manual check needed for most
    if "Ghavami" in file_path.name:
         new_header = new_header.replace("Not Identified", "Khosrow Ghavami; Albanise B. Marinho")
         new_header += f"\ninstituicao_origem: PUC-Rio"
    new_header += f"\nequipe_tecnica: UnB/UFAC/UFRR"
    new_header += f"\nano_publicacao: '{year}'"
    new_header += "\n---\n"

    # 5. Filter Content
    body = content.split("---", 2)[-1].strip()
    
    # Remove AI greetings
    body = re.sub(r"Com certeza.*?\n", "", body)
    body = re.sub(r"Com base no texto.*?\n", "", body)
    
    # Remove redundant title/reference if it starts with # or ## and repeats name
    body_lines = body.split('\n')
    filtered_body = []
    for line in body_lines:
        if line.startswith("#") and any(word in line.lower() for word in clean_name.lower().split()):
            continue
        if "Referência:" in line or "Resumo do Trabalho Original" in line:
            continue
        if line.startswith("- **📍 Localização Original:**"):
            continue
        if line.startswith("- **🔍 Prévia do Conteúdo:**"):
            continue
        if "Status de Tabela:" in line or "Requer curadoria" in line:
            continue
        filtered_body.append(line)
        
    final_content = new_header + "\n" + '\n'.join(filtered_body).strip()
    file_path.write_text(final_content + "\n", encoding="utf-8")
    return is_preview

def update_index(hidden_previews):
    print(f"Updating index: {INDEX_PATH}")
    content = INDEX_PATH.read_text(encoding="utf-8")
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        if "| [" in line and ".md" in line:
            # Check if filename in index matches a hidden preview
            for filename in hidden_previews:
                if filename in line:
                    # Unlink review
                    # Column format: | Icon | Title | Tags | [Link] | [Review] |
                    parts = line.split('|')
                    if len(parts) >= 6:
                        parts[5] = " --- " 
                        line = '|'.join(parts)
                    break
        new_lines.append(line)
        
    INDEX_PATH.write_text('\n'.join(new_lines), encoding="utf-8")

if __name__ == "__main__":
    hidden_previews = []
    for file_path in REVIEWS_DIR.glob("*.md"):
        if refine_file(file_path):
            hidden_previews.append(file_path.name)
    
    update_index(hidden_previews)
    print("\nRefinement and unlinking complete.")
