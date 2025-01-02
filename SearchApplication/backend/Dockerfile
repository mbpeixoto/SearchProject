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

# Expor a porta padrão do FastAPI
EXPOSE 8000

ENV PYTHONPATH=/app

# Comando para iniciar o aplicativo
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
