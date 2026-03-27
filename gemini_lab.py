from google import genai
import sys, os

# 1. Configuração com o Client moderno
client = genai.Client(api_key=os.environ.get("AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"))

# 2. Atualizado para o modelo de ponta que sua chave liberou
MODEL_ID = "models/gemini-2.5-flash"

def perguntar():
    if len(sys.argv) > 1:
        prompt_usuario = sys.argv[1]
        contexto = "Atue como pesquisador sênior especialista em bioeconomia e desenvolvimento sustentável com foco em aptoveitamento de biomassa e créditos de carbono. "
        
        try:
            # 3. Chamada de geração de conteúdo
            response = client.models.generate_content(
                model=MODEL_ID, 
                contents=contexto + prompt_usuario
            )
            
            # 4. Acesso ao texto da resposta
            print(f"\n✨ RESPOSTA GEMINI 2.5 (Projeto WTF):\n{response.text}")
                
        except Exception as e:
            print(f"❌ Erro na chamada: {e}")
    else:
        print("Uso: python gemini_lab.py 'Sua pergunta aqui'")

if __name__ == "__main__":
    perguntar()


# python gemini_lab.py "$(cat arquivo.txt) --- [PROMPT]"