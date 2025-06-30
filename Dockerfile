# Use a imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requirements para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação para o container
COPY ./app /app

# Define o comando para executar a aplicação Flask
CMD ["flask", "--app", "app.py", "--debug", "run", "--host", "0.0.0.0", "--port", "5000"]