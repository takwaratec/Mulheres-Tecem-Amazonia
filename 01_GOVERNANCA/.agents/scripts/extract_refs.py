import os
import re

def extract_references(directory):
    references = set()
    for root, dirs, files in os.walk(directory):
        if 'historico' in root or '.agents' in root:
            continue
        for file in files:
            if file.endswith('.md') and not file.startswith('BD_referencias'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Look for sections like ## Referências, ## Bibliografia, etc.
                    matches = re.finditer(r'^##\s*(Referências|Bibliografia|Referências Bibliográficas|Referências Institucionais).*?\n(.*?)(?=\n##|\Z)', content, re.MULTILINE | re.IGNORECASE | re.DOTALL)
                    for match in matches:
                        ref_block = match.group(2).strip()
                        # Some references are bullet points or numbered lists, or just paragraphs
                        lines = ref_block.split('\n')
                        for line in lines:
                            line = line.strip()
                            if not line or line.startswith('#'):
                                continue
                            if len(line) > 10 and not line.startswith('---'):
                                # Strip bullets
                                line = re.sub(r'^[*+\-]\s+', '', line)
                                line = re.sub(r'^\d+\.\s+', '', line)
                                references.add(line)
    return references

refs = extract_references('.')
for r in sorted(refs):
    print(r)
