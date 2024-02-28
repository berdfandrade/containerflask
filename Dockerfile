# Use uma imagem base Python
FROM python:3.9

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do aplicativo
RUN pip install -r requirements.txt

# Copia todo o código do aplicativo para o diretório de trabalho
COPY . .

# Comando para iniciar o servidor Flask
CMD ["python", "app.py"]
