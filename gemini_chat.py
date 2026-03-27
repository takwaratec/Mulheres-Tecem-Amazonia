import google.generativeai as genai
import sys, os

genai.configure(api_key=os.environ["AIzaSyDnUer8X3QiY0dJtK26xL9z8hGxbtm3R8A"])
model = genai.GenerativeModel('gemini-1.5-flash')

if len(sys.argv) > 1:
    response = model.generate_content(sys.argv[1])
    print(f"\n✨ Gemini:\n{response.text}")