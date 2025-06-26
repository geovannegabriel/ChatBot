# 🤖 Chatbot com OpenAI em Python

Este projeto é um chatbot funcional de terminal criado em Python, utilizando a API oficial da OpenAI (modelo `gpt-3.5-turbo`). A aplicação permite conversas contínuas com o modelo, armazenando o contexto da conversa e oferecendo uma interação fluida com o usuário.

---

## 🚀 Funcionalidades

- Integração com a API da OpenAI (gpt-3.5-turbo)
- Histórico de conversas mantido durante a execução
- Comando para encerrar o chat (`sair`, `SAIR`, `Sair`, `exit`, etc.)
- Execução 100% via terminal
- Código limpo, organizado e com boas práticas

---

## 🧠 Pré-requisitos

- Python 3.8+
- Conta na [OpenAI](https://platform.openai.com/)
- Chave de API ativa

---

## ⚙️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot-openai-python.git
cd chatbot-openai-python
Crie um ambiente virtual:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate
Instale a biblioteca da OpenAI:

bash
Copiar
Editar
pip install openai
Crie um arquivo .env (opcional) e adicione sua chave:

env
Copiar
Editar
OPENAI_API_KEY=sua-chave-aqui
Ou, no código chatbot.py, insira sua chave diretamente.

▶️ Como usar
Execute o chatbot com:

bash
Copiar
Editar
python chatbot.py
Digite sua mensagem no terminal e receba uma resposta. Para encerrar, digite sair.

💡 Exemplo de uso
bash
Copiar
Editar
Você: Qual foi o primeiro presidente do Brasil?
Chatbot: O primeiro presidente do Brasil foi Deodoro da Fonseca...
🔒 Segurança
Nunca compartilhe sua chave da OpenAI publicamente.
Use arquivos .env e adicione ao .gitignore para manter a chave oculta.

📁 Estrutura do Projeto
bash
Copiar
Editar
chatbot-openai-python/
├── chatbot.py
├── venv/
├── README.md
└── .env (opcional)
📌 Autor
Gabriel 

🧠 Ideias futuras
Interface com Flask ou Streamlit

Persistência de histórico em arquivo

Testes unitários



---
