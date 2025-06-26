from openai import OpenAI

# Substitua pela sua chave real (Não coloquei uma chave real por questão de segurança)
client = OpenAI(api_key="SUA_CHAVE_AQUI")


lista_mensagens = []

def enviar_mensagem(mensagem_usuario):
    lista_mensagens.append({"role": "user", "content": mensagem_usuario})
    
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens
    )
    
    mensagem_resposta = resposta.choices[0].message
    lista_mensagens.append({"role": "assistant", "content": mensagem_resposta.content})
    
    return mensagem_resposta.content

print("Digite sua mensagem ou caso deseje sair digite 'sair'.")

while True:
    texto = input("Você: ").strip().lower()
    
    if texto in ["sair", "exit", "quit"]:
        print("Encerrando o chatbot. Até a próxima!")
        break
    
    resposta = enviar_mensagem(texto)
    print("Chatbot:", resposta)
