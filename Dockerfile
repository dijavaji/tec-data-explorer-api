# Usar imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app
#actualizamos pip
RUN pip install --upgrade pip
# Copia los archivos de requerimientos
COPY requirements.txt .
# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m spacy download es_core_news_sm

# Copia la aplicacion al contenedor
COPY . .

# Expone el puerto en el que tu aplicación va a correr
EXPOSE 8000

# Define el comando para ejecutar tu aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]