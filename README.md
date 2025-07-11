# municipios-brasileiros

Repositório do projeto final da disciplina de Projeto e Arquitetura de Software.

## Sobre o Projeto

Esta aplicação é desenvolvida em Python utilizando o framework Flask e PostgreSQL para o banco de dados, com Bootstrap para o front-end. O objetivo é fornecer uma interface web para visualização e consulta de dados de municípios brasileiros.

## Descrição das Tecnologias/Linguagens Usadas na Implementação

### Backend
- **Python 3.x**: Linguagem de programação principal
- **Flask 3.1.1**: Framework web para desenvolvimento da aplicação
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional
- **psycopg2-binary 2.9.10**: Adaptador PostgreSQL para Python
- **python-dotenv 1.1.1**: Gerenciamento de variáveis de ambiente

### Frontend
- **HTML5**: Estruturação das páginas web
- **Bootstrap 5.3.3**: Framework CSS responsivo
- **JavaScript/jQuery 3.7.1**: Interatividade e requisições AJAX
- **Jinja2**: Engine de templates do Flask

### Infraestrutura
- **Docker & Docker Compose**: Containerização e orquestração
- **Git**: Controle de versão

## Descrição Geral da Estrutura do Projeto com Caracterização da Arquitetura Implementada e Padrões Utilizados

### Arquitetura Implementada

O projeto utiliza uma **arquitetura em camadas** baseada no padrão **MVC (Model-View-Controller)** combinado com os padrões **Repository** e **DAO (Data Access Object)** para garantir separação de responsabilidades e facilitar manutenção.

### Padrões Utilizados

1. **MVC (Model-View-Controller)**
   - **Models**: Entidades de negócio (`Municipio`, `Capital`, `Populacao`)
   - **Views**: Templates HTML com Jinja2
   - **Controllers**: Coordenação entre View e Model

2. **Repository Pattern**
   - Abstração do acesso a dados
   - Centralização das regras de negócio
   - Facilita testes e manutenção

3. **DAO (Data Access Object)**
   - Acesso direto ao banco de dados
   - Mapeamento objeto-relacional
   - Isolamento das queries SQL

4. **Factory Pattern**
   - Criação da aplicação Flask
   - Configuração centralizada

5. **Dependency Injection**
   - Gerenciamento via contexto Flask
   - Conexões de banco automáticas

## Estrutura do Projeto

```
municipios-brasileiros/
├── app/
│   ├── controllers/              # Lógica das rotas e controllers
│   ├── dao/                      # Data Access Objects (acesso a dados)
│   ├── models/                   # Modelos de dados
│   ├── repository/               # Repositórios de dados
│   ├── static/                   # Arquivos estáticos (CSS, JS, imagens)
│   ├── views/                    # Templates HTML (Jinja2)
│   ├── app.py                    # Inicialização do app Flask
│   ├── db.py                     # Gerenciamento de conexões de banco
│   ├── routes.py                 # Definição das rotas principais
│   └── settings.py               # Configurações globais da aplicação
├── data/
│   └── municipios.csv            # Dataset dos municípios brasileiros
├── scripts/
│   └── initdb.sql               # Script de inicialização do PostgreSQL
├── docker-compose.yaml          # Orquestração de contêineres
├── Dockerfile                   # Imagem Docker da aplicação
├── requirements.txt             # Dependências Python
├── .gitignore
└── README.md
```

### Organização das Camadas

- **`app/`** — Módulo principal da aplicação Flask
  - **`controllers/`** — Coordenam requisições HTTP e respostas
  - **`dao/`** — Acesso direto ao banco de dados e queries SQL
  - **`models/`** — Entidades de negócio (Municipio, Capital, Populacao)
  - **`repository/`** — Regras de negócio e validações
  - **`static/`** — Scripts JavaScript para interatividade AJAX
  - **`views/`** — Templates HTML com Bootstrap e Jinja2
  - **`app.py`** — Factory da aplicação e configuração inicial
  - **`db.py`** — Gerenciamento de conexões PostgreSQL
  - **`routes.py`** — Mapeamento de URLs para controllers
  - **`settings.py`** — Configurações e variáveis de ambiente

## Como Executar

### Execução com Docker

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/sfrederico/municipios-brasileiros.git
   cd municipios-brasileiros
   ```

2. **Configure as variáveis de ambiente:**
   ```bash
   # Crie um arquivo .env com as configurações do banco
   ```

3. **Execute com Docker Compose:**
   ```bash
   docker-compose up --build
   ```

4. **Acesse a aplicação:** http://localhost:5000


## Tecnologias Utilizadas
- Python 3
- Flask
- PostgreSQL
- Bootstrap (via CDN)
- Docker

