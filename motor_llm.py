# file  : motor_llm.py
# autor : Paulinho Neto (Carpc)
# date  : 27-10-2026

import os
from dotenv import load_dotenv
import freelm

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

llm = freelm.FreeLLM.from_env()

def perguntar_ia(prompt: str, contexto: str = "", usar_ferramentas: bool = False):
    """
    Função genérica para os laboratórios usarem.
    - prompt: A tarefa do usuário (ex: "Resuma as mensagens").
    - contexto: O documento/mensagem onde a injeção está escondida (Opcional).
    - usar_ferramentas: Força um modelo com suporte a Tool Calling.
    """
    modelo = "chat:tools" if usar_ferramentas else "auto"
    mensagens = []
    
    # 1. Regra de idioma (só se não for usar ferramentas)
    if not usar_ferramentas:
        mensagens.append({
            "role": "system", 
            "content": "Responda sempre no mesmo idioma da mensagem do usuário."
        })
    
    # 2. Se houver contexto (Lab de Injeção Indireta), ele entra como 'system' ou 'user'
    if contexto:
        # O contexto entra como um documento confiável que a IA precisa ler
        mensagens.append({"role": "user", "content": f"Contexto para análise:\n{contexto}"})
    
    # 3. O pedido do usuário (a tarefa)
    mensagens.append({"role": "user", "content": prompt})
    
    try:
        resposta = llm.chat(mensagens, model=modelo)
        return resposta.text
    except Exception as e:
        return f"Erro na IA: {e}"