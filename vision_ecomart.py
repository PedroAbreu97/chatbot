from openai import OpenAI
from dotenv import load_dotenv
import os
from time import sleep
from helpers import encodar_imagem

load_dotenv()

cliente = OpenAI(api_key="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")
modelo = "gpt-4-1106-preview"

def analisar_imagem(caminho_imagem):
    prompt = """"
        Assuma que você é um assistente de chatbot e que provaelmente o usuário está enviado a foto de
        um produto. Faça uma análise dele, e se for um produto com defeito, emita um parecer. Assuma que você sabe e
        processou uma imagem com o Vision e a resposta será informada no formato de saída.

        # FORMATO DA RESPOSTA
    
        Minha análise para imagem consiste em: Parecer com indicações do defeito ou descrição do produto (se não houver defeito)

        ## Descreva a imagem
        coloque a descrição aqui
    """

    imagem_base64 = encodar_imagem(caminho_imagem)

    resposta = cliente.chat.completions.create(
        model=modelo,
        messages=[
            {
            "role": "user",
            "content": [
                {
                    "type": "text", "text": prompt
                },
                {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{imagem_base64}",
                },
                },
            ],
            }
        ],
        max_tokens=300,
        )
    return resposta.choices[0].message.content

print(analisar_imagem("dados/new_caneca.png"))