# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы requirements.txt и устанавливаем зависимости Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальную часть приложения в контейнер
COPY . .

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Запускаем приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
