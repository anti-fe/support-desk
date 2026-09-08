# Используем официальный образ Python
FROM python:3.12-slim
# Устанавливаем рабочую директорию внутри контейнера.
WORKDIR /app
# Копируем файл зависимостей отдельно
COPY requirements.txt .
# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r requirements.txt
# Копируем исходный код приложения в контейнер
COPY app ./app
# Сообщаем Docker, что приложение использует порт 8000
EXPOSE 8000
# Запускаем FastAPI через Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]