import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analisar_curriculo(texto: str) -> dict:
    prompt = f"""
    Você é um recrutador sênior com 15 anos de experiência.
    Analise o currículo abaixo e responda APENAS com um JSON válido, sem texto adicional.

    O JSON deve ter exatamente essa estrutura:
    {{
        "pontos_fortes": ["...", "..."],
        "pontos_fracos": ["...", "..."],
        "sugestoes": ["...", "..."],
        "nota_geral": <número de 1 a 10 baseado na qualidade real do currículo, sendo 1 péssimo e 10 excelente>
    }}

    Currículo:
    {texto}
    """

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    texto_resposta = resposta.choices[0].message.content.strip()

    if texto_resposta.startswith("```"):
        texto_resposta = texto_resposta.split("```")[1]
        if texto_resposta.startswith("json"):
            texto_resposta = texto_resposta[4:]

    return json.loads(texto_resposta)