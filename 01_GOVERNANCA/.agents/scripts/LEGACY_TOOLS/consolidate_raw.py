import os
from pathlib import Path
import shutil
import re

# Configuration
REPO_ROOT = Path("/Users/fabiotakwara/Documents/GitHub/UnB/Mulheres-Tecem-Amazonia")
SOURCE_DIR = REPO_ROOT / "04_PESQUISA_ANDAMENTO/TRANSCRIPT"
DEST_DIR = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/01_RAW_TRANSCRIPTS"

# Ensure destination exists
DEST_DIR.mkdir(parents=True, exist_ok=True)

def normalize_filename(name):
    # Remove existing prefixes
    name = name.replace("WTF_RAW_RAW_", "").replace("WTF_RAW_", "").replace("RAW_", "")
    # Remove extension to re-standardize
    name = Path(name).stem.replace(".pdf", "")
    return f"WTF_RAW_{name}.txt"

def consolidate():
    print(f"Consolidating transcripts to {DEST_DIR}...")
    
    # Track files already processed to avoid duplicates
    processed_files = set()
    
    # 1. Gather all potential transcripts (.txt and .md that are actually transcripts)
    # We walk the entire TRANSCRIPT dir including AMAZONIA_GESTORAS
    for file_path in SOURCE_DIR.glob("**/*"):
        if file_path.is_dir() or file_path.name.startswith(".") or ".ARCHIVE" in str(file_path):
            continue
            
        if file_path.suffix in [".txt", ".md"] and not file_path.name.startswith("WTF_RES_"):
            # Skip metadata files
            if file_path.name in ["BIBLIOGRAFIA.md", "CATALOGO.md", "README.md", "BD_referencias-acervo.md"]:
                continue
                
            new_name = normalize_filename(file_path.name)
            dest_path = DEST_DIR / new_name
            
            print(f" Moving: {file_path.name} -> {new_name}")
            
            # Read content to ensure we keep the standardized YAML header from the source
            content = file_path.read_text(encoding="utf-8")
            
            # If it's a .md that was accidentally named, we keep the content but save as .txt
            dest_path.write_text(content, encoding="utf-8")
            
            # If it was moved successfully and it's from the specified source, we can delete the source
            # But safer to move and then clean.
            processed_files.add(file_path)

    # 2. Handle files already in DEST_DIR that might be duplicates or poorly named
    for file_path in DEST_DIR.glob("*"):
        if file_path.name.startswith("WTF_RAW_RAW_"):
            new_name = normalize_filename(file_path.name)
            new_path = DEST_DIR / new_name
            if new_path != file_path:
                print(f" Renaming in-place: {file_path.name} -> {new_name}")
                # If target exists, merge or overwrite? User said eliminate duplicates.
                # Usually the ones in SOURCE (TRANSCRIPT/) are more up-to-date with headers.
                if new_path.exists():
                    file_path.unlink()
                else:
                    file_path.rename(new_path)

def clean_source():
    print("Cleaning source directories...")
    # Move MD catalogs from AMAZONIA_GESTORAS to METADATA_CATALOG
    metadata_dest = REPO_ROOT / "04_PESQUISA_ANDAMENTO/ACERVO_DIGITAL_WTF/03_METADATA_CATALOG"
    for file_path in (SOURCE_DIR / "AMAZONIA_GESTORAS").glob("*.md"):
        if file_path.name in ["BIBLIOGRAFIA.md", "CATALOGO.md", "CATALOGO2.md", "BD_referencias-acervo.md", "BIBLIOGRAPHY_CONSOLIDATED.md"]:
             print(f" Archiving catalog: {file_path.name}")
             dest = metadata_dest / f"LEGACY_{file_path.name}"
             if not dest.exists():
                 file_path.rename(dest)
             else:
                 file_path.unlink()

if __name__ == "__main__":
    consolidate()
    clean_source()
    print("\nConsolidation complete.")
