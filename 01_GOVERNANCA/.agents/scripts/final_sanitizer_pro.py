import os
import re

FINAL_BASE = '.'
# Termos Proibidos (Case Insensitive)
PURGE_TERMS = [r'(?i)Takwara', r'(?i)Mestre 5\.2', r'(?i)Mestre 5\.1', r'(?i)Tak-', r'(?i)PAR 5\.1']

def sanitize_repo_pro():
    print("🧹 Iniciando Sanitização PROFISSIONAL (Case Insensitive)...")
    
    for root, dirs, files in os.walk(FINAL_BASE, topdown=False):
        for name in files + dirs:
            old_path = os.path.join(root, name)
            new_name = name
            
            for pattern in PURGE_TERMS:
                new_name = re.sub(pattern, '', new_name)
            
            # Limpeza de caracteres residuais
            new_name = new_name.replace('__', '_').replace('..', '.').strip('_- ')
            
            if not new_name:
                new_name = "asset_" + os.path.splitext(name)[0] + os.path.splitext(name)[1]
                
            if new_name != name:
                new_path = os.path.join(root, new_name)
                if os.path.exists(new_path) and new_path != old_path:
                    new_path = os.path.join(root, "v2_" + new_name)
                
                try:
                    os.rename(old_path, new_path)
                    print(f"🔄 Renomeado: {name} -> {new_name}")
                except Exception as e:
                    print(f"⚠️ Erro ao renomear {name}: {e}")

if __name__ == "__main__":
    sanitize_repo_pro()
