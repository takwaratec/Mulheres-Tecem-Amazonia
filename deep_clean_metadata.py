import os
import re
from pathlib import Path

# Configuration
REPO_ROOT = Path("/Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia")
REVIEWS_DIR = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/02_TECHNICAL_REVIEWS"
RAW_DIR = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS"

INSTITUTIONAL_AUTHOR_REVIEW = "Equipe Técnica WTF (UnB/UFAC/UFRR)"
INSTITUTIONAL_AUTHOR_RAW = "Acervo Digital WTF"

def deep_clean_file(file_path, institutional_author):
    print(f" Deep cleaning: {file_path.name}")
    content = file_path.read_text(encoding="utf-8")
    
    # 1. Fix YAML Header
    # Remove 'citacao' and 'autor' traces
    lines = content.split('\n')
    new_lines = []
    in_header = False
    header_done = False
    
    for line in lines:
        if line.strip() == "---" and not header_done:
            if not in_header:
                in_header = True
                new_lines.append(line)
                continue
            else:
                in_header = False
                header_done = True
                new_lines.append(line)
                continue
        
        if in_header:
            if line.startswith("autor:"):
                new_lines.append(f"autor: {institutional_author}")
            elif line.startswith("citacao:"):
                continue # Remove citacao line
            elif line.strip() and not line.startswith(" "): # Skip continuation lines of citacao
                new_lines.append(line)
            elif line.startswith(" "): # Continuation of previous line (potential citacao multiline)
                if len(new_lines) > 0 and not new_lines[-1].startswith("citacao:"):
                    # Only keep if previous line wasn't removed
                    if "citacao:" not in str(lines[lines.index(line)-1]):
                         new_lines.append(line)
                continue
        else:
            # 2. Remove AI Greetings and Intro logic
            # Skip lines that look like AI self-introductions
            if "Com certeza" in line or "Com base no texto" in line or "Agindo como" in line or "apresento a análise" in line:
                continue
            # Also handle multiline AI intro if it's the first non-empty line after header
            new_lines.append(line)

    # Reassemble and strip excessive whitespace
    cleaned_content = '\n'.join(new_lines).strip()
    
    # Ad-hoc fix for specific files mentioned by user (like Ghavami)
    if "Ghavami" in file_path.name:
        cleaned_content = cleaned_content.replace("'2025'", "'2003'").replace("data: 2025", "data: 2003")

    file_path.write_text(cleaned_content + "\n", encoding="utf-8")

def run_cleanup():
    for file_path in REVIEWS_DIR.glob("*.md"):
        deep_clean_file(file_path, INSTITUTIONAL_AUTHOR_REVIEW)
        
    for file_path in RAW_DIR.glob("*.txt"):
        deep_clean_file(file_path, INSTITUTIONAL_AUTHOR_RAW)

if __name__ == "__main__":
    run_cleanup()
    print("\nDeep cleaning of metadata complete.")
