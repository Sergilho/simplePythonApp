# Define a imagem base
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Instala as dependências do Python especificadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todos os arquivos do diretório atual para dentro do diretório /app do container
COPY . .

# Define a porta em que a aplicação vai escutar
EXPOSE 5000

# Define o comando que será executado quando o container for iniciado
CMD [ "python", "./app.py" ]
