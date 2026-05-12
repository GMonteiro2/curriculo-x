# Currículo X 🎯

Análise inteligente de currículos com IA. Cole o texto ou envie um arquivo PDF/TXT e receba em segundos uma análise detalhada com pontos fortes, pontos fracos, sugestões de melhoria e uma nota geral.

## 🖥️ Demo

<img width="1142" height="569" alt="image" src="https://github.com/user-attachments/assets/28ccb849-4c79-451c-9680-01dc26402566" />


<img width="1108" height="508" alt="image" src="https://github.com/user-attachments/assets/49315c97-fe45-4eb9-b5e5-5c0839aa2879" />


## 🚀 Tecnologias

- **FastAPI** — framework web moderno e de alta performance
- **Pydantic** — validação de dados e modelagem
- **Groq + LLaMA 3.3** — modelo de linguagem para análise inteligente
- **Jinja2** — templates HTML
- **Python-dotenv** — gerenciamento de variáveis de ambiente

## ⚙️ Como rodar localmente

**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/curriculo-x.git
cd curriculo-x
```

**2. Instale as dependências**
```bash
pip install -r requirements.txt
```

**3. Configure as variáveis de ambiente**
```bash
cp .env.example .env
```
Edite o `.env` e adicione sua chave da API do Groq.

**4. Suba o servidor**
```bash
python -m uvicorn app.main:app --reload
```

**5. Acesse no navegador**
http://127.0.0.1:8000

## 📁 Estrutura do projeto
curriculo-x/
├── app/
│   ├── static/
│   │   ├── style.css
│   │   └── script.js
│   ├── templates/
│   │   └── index.html
│   ├── analyzer.py   # lógica de integração com a IA
│   ├── models.py     # modelos Pydantic
│   ├── routes.py     # rotas da API
│   └── main.py       # ponto de entrada
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

## 🔌 API

### `POST /api/analisar`
Analisa um currículo em texto.

**Body:**
```json
{
  "curriculo": "texto do currículo aqui"
}
```

### `POST /api/analisar-arquivo`
Analisa um currículo via upload de arquivo PDF ou TXT.

**Form data:** `arquivo` (PDF ou TXT)

**Resposta de ambos os endpoints:**
```json
{
  "pontos_fortes": ["..."],
  "pontos_fracos": ["..."],
  "sugestoes": ["..."],
  "nota_geral": 8
}
```

## 📝 Licença
MIT

Tem um detalhe importante — cria também um arquivo .env.example na raiz do projeto com esse conteúdo:
GROQ_API_KEY=sua_chave_aqui

Esse arquivo vai pro GitHub no lugar do .env real, é a forma profissional de mostrar quais variáveis o projeto precisa sem expor as chaves. Qualquer pessoa que clonar o projeto sabe exatamente o que configurar.
