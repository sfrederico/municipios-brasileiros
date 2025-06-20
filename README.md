# municipios-brasileiros

Repositório do projeto final da disciplina de Projeto e Arquitetura de Software.

## Sobre o Projeto

Esta aplicação é desenvolvida em Python utilizando o framework Flask e Bootstrap para o front-end. O objetivo é fornecer uma interface web para visualização e manipulação de dados de municípios brasileiros.

## Estrutura do Projeto

```
municipios-brasileiros/
├── app/
│   ├── controllers/
│   ├── dao/
│   ├── models/
│   ├── repository/
│   ├── static/
│   |── views/
│   |── app.py
│   |── routes.py
│   └── settings.py
├── requirements.txt
├── .gitignore
└── README.md
```

- `app/` — Módulo principal da aplicação Flask
  - `controllers/` — Lógica das rotas e controllers
  - `dao/` — Data Access Objects (acesso a dados)
  - `models/` — Modelos de dados
  - `repository/` — Repositórios de dados
  - `static/` — Arquivos estáticos (CSS, JS, imagens)
  - `views/` — Templates HTML (Jinja2)
  - `app.py` — Inicialização do app Flask
  - `routes.py` — Definição das rotas principais
  - `settings.py` — Configurações globais da aplicação

  

## Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/sfrederico/municipios-brasileiros.git
   cd municipios-brasileiros
   ```
2. **Crie um ambiente virtual:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Execute a aplicação:**
   ```bash
   cd app
   flask run --app app.py --debug
   ```
   Acesse em: http://127.0.0.1:5000/

## Tecnologias Utilizadas
- Python 3
- Flask
- Bootstrap (via CDN)

