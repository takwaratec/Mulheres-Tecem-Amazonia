import os

def generate_index():
    bib_file = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/03_METADATA_CATALOG/WTF_BIBLIOGRAPHY_CONSOLIDATED.md"
    transcripts_dir = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS"
    reviews_dir = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"
    index_file = "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/03_METADATA_CATALOG/WTF_INDEX_ACERVO.md"

    transcripts = os.listdir(transcripts_dir)
    reviews = os.listdir(reviews_dir)

    # Management Team Names
    MANAGEMENT_TEAM = ["Araújo", "Ferko", "Carvalho", "Cruz", "Vargas", "Sonia", "Tânia", "Geórgia", "Vanessa"]
    PRIMARY_TERRITORIES = ["Acre", "Amazônia Legal", "Indígena", "Quilombola", "Amazonas"]
    # Technical Categories
    CAT_BAMBU = ["Bambu", "Bamboo", "Dendrocalamus", "Guadua", "Bambusa"]
    CAT_BIOPOL = ["PU", "Poliuretano", "Resina", "Vegetal", "Mamona", "Castor", "Imperveg", "Bio-polímero"]
    CAT_ENG = ["Resistência", "Flexão", "Compressão", "Ensaio", "Carga", "Tração", "Estrutura", "Cálculo"]
    CAT_MANUAIS = ["Manual", "Cartilha", "Guia", "EMBRAPA", "INBAR", "ISO", "ABNT", "Norma", "Standard", "Protocolo"]

    index_content = """# 🗂️ Master Index: Acervo Digital WTF

Este índice vincula a bibliografia consolidada aos respectivos transcritos e resumos estratégicos (Padrão BNDES).

**Legenda de Referência Primária:**
- ⭐ **Gestão**: Artigo de autoria ou coautoria da equipe de gestoras (Sonia, Tania, Georgia, Vanessa).
- 📍 **Território**: Referência direta ao Acre, Amazônia Legal ou contextos Indígenas/Quilombolas.
- 🎋 **Bambu**: Foco em tecnologias e espécies de bambu.
- ⚗️ **Bio-Polímeros**: Pesquisa em PU vegetal, resinas e revestimentos biobaseados.
- 🏗️ **Engenharia**: Ensaios de resistência, cálculo estrutural e performance.
- 📖 **Manuais/Normas**: Manuais técnicos, cartilhas EMBRAPA/INBAR e Normas Técnicas (ISO/ABNT).

| Título do Documento | Ref. Primária | Transcrito Bruto | Resumo Estratégico (P&D) |
|:---|:---|:---|:---|
"""

    with open(bib_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_title = ""
    current_authors = ""
    for i, line in enumerate(lines):
        if line.startswith("- **Title**:") or line.startswith("- **Título**:"):
            current_title = line.split(":", 1)[1].strip()
            
            # Fetch authors (look ahead a bit)
            current_authors = ""
            for next_line in lines[i:i+5]:
                if "**Authors**:" in next_line or "**Autores**:" in next_line:
                    current_authors = next_line.split(":", 1)[1].strip()
                    break

            # Identify Primary Reference
            import re
            def has_term(term_list, text):
                for term in term_list:
                    if len(term) <= 3:
                        if re.search(rf'\b{re.escape(term)}\b', text, re.IGNORECASE):
                            return True
                    else:
                        if term.lower() in text.lower():
                            return True
                return False

            is_management = any(name.lower() in current_authors.lower() for name in MANAGEMENT_TEAM)
            is_territory = has_term(PRIMARY_TERRITORIES, current_title)
            is_bambu = has_term(CAT_BAMBU, current_title)
            is_biopol = has_term(CAT_BIOPOL, current_title)
            is_eng = has_term(CAT_ENG, current_title)
            is_manuais = has_term(CAT_MANUAIS, current_title)
            
            ref_primaria = []
            if is_management: ref_primaria.append("⭐")
            if is_territory: ref_primaria.append("📍")
            if is_bambu: ref_primaria.append("🎋")
            if is_biopol: ref_primaria.append("⚗️")
            if is_eng: ref_primaria.append("🏗️")
            if is_manuais: ref_primaria.append("📖")
            
            ref_str = " ".join(ref_primaria) if ref_primaria else "-"

            # Simple matching logic based on keywords in title
            # Search for transcript
            matched_transcript = "Not Found"
            for trans in transcripts:
                if any(word.lower() in trans.lower() for word in current_title.split()[:3] if len(word) > 3):
                    matched_transcript = f"[Transcript](../01_RAW_TRANSCRIPTS/{trans})"
                    break
            
            # Search for review
            matched_review = "Not Found"
            for rev in reviews:
                if any(word.lower() in rev.lower() for word in current_title.split()[:3] if len(word) > 3):
                    matched_review = f"[Review](../02_TECHNICAL_REVIEWS/{rev})"
                    break
            
            index_content += f"| {current_title} | {ref_str} | {matched_transcript} | {matched_review} |\n"

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    return index_file

if __name__ == "__main__":
    path = generate_index()
    print(f"Index generated at: {path}")
