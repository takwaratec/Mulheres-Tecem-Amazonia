import os
import re
import yaml
from pathlib import Path

# Configuration
REPO_ROOT = Path("/Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia")
TRANSCRIPT_DIR = REPO_ROOT / "04_PESQUISA_ANDAMENTO/TRANSCRIPT"
REVIEWS_DIR = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"
BIBLIOGRAPHY_FILE = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/03_METADATA_CATALOG/WTF_BIBLIOGRAPHY_CONSOLIDATED.md"

STANDARD_INSTITUTION = "Consórcio UnB/UFAC/UFRR"
STANDARD_PROJECT = "Mulheres Que Tecem a Floresta"
STANDARD_TEAM = "Gestão e Parceria Regional"

def get_bibliography_data():
    """Simple parser for bibliography data to match titles with authors/years."""
    if not BIBLIOGRAPHY_FILE.exists():
        return {}
    
    content = BIBLIOGRAPHY_FILE.read_text(encoding="utf-8")
    data = {}
    
    # Very simple extraction logic for this specific file structure
    entries = re.split(r'\n- \*\*Title\*\*: ', content)
    for entry in entries[1:]:
        lines = entry.split('\n')
        title = lines[0].strip()
        year = ""
        authors = ""
        for line in lines:
            if "Year" in line:
                year_match = re.search(r'\d{4}', line)
                if year_match:
                    year = year_match.group(0)
            if "Authors" in line:
                authors = line.split(': ')[1].strip()
        
        data[title.lower()] = {"year": year, "authors": authors}
    return data

def create_header(file_path, type_label, bib_data):
    filename = file_path.name
    # Guess data from filename if not in bib
    year_match = re.search(r'20\d{2}', filename)
    year = year_match.group(0) if year_match else "2025"
    
    # Placeholder citation logic
    clean_name = filename.replace("RAW_", "").replace("WTF_RES_", "").replace(".pdf.txt", "").replace(".txt", "").replace(".md", "").replace("_", " ")
    
    header = {
        "projeto": STANDARD_PROJECT,
        "instituicao": STANDARD_INSTITUTION,
        "equipe": STANDARD_TEAM,
        "tipo": type_label,
        "autor": "Antigravity (AI) & Fabio Takwara (Coordenação)" if "WTF_RES" in filename else "Não identificado",
        "data": year,
        "citacao": f"TAKWARA, F. [et al.]. {clean_name}. {STANDARD_INSTITUTION}, {year}."
    }
    
    # Try to refine with bibliography data
    for title, info in bib_data.items():
        if title in filename.lower() or filename.lower().replace("_", " ") in title:
            if info["authors"]:
                header["autor"] = info["authors"]
            if info["year"]:
                header["data"] = info["year"]
            header["citacao"] = f"{header['autor'].upper()}. {title}. {STANDARD_INSTITUTION}, {header['data']}."
            break

    return "---\n" + yaml.dump(header, allow_unicode=True, sort_keys=False) + "---\n"

def process_directory(directory, type_label, bib_data, extension="*"):
    print(f"Processing {directory}...")
    for file_path in directory.glob(f"**/{extension}"):
        if file_path.is_dir() or file_path.name.startswith("."):
            continue
            
        print(f" Updating: {file_path.name}")
        content = file_path.read_text(encoding="utf-8")
        
        # Strip existing YAML if present
        if content.startswith("---"):
            try:
                _, _, content = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
            except ValueError:
                pass # Not a valid YAML block at start
        
        new_header = create_header(file_path, type_label, bib_data)
        file_path.write_text(new_header + content.strip(), encoding="utf-8")

def clean_redundant_files():
    """Moves duplicate or redundant files (e.g. '(1).pdf.txt') to a .ARCHIVE folder."""
    archive_dir = TRANSCRIPT_DIR / ".ARCHIVE"
    archive_dir.mkdir(exist_ok=True)
    
    print(f"Cleaning redundant files in {TRANSCRIPT_DIR}...")
    for file_path in TRANSCRIPT_DIR.glob("**/*.txt"):
        if "(1)" in file_path.name or "copy" in file_path.name.lower():
            print(f" Archiving redundant: {file_path.name}")
            file_path.rename(archive_dir / file_path.name)

if __name__ == "__main__":
    bib_data = get_bibliography_data()
    
    # Step 0: Cleaning
    clean_redundant_files()
    
    # Step 1: Process Reviews
    process_directory(REVIEWS_DIR, "Acervo de Pesquisa (Review Técnica)", bib_data, extension="*.md")
    
    # Step 2: Process Transcripts
    process_directory(TRANSCRIPT_DIR, "Acervo de Consulta RAW (Transcrição)", bib_data, extension="*.txt")

    print("\nMetadata standardization and cleaning complete.")
