# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Criar diretório de trabalho
WORKDIR /app

# Copiar os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o contêiner
COPY . .

# Expor a porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar o Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
