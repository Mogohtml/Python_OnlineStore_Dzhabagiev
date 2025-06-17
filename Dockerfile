FROM python:3.12
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 8000
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=webstore.settings

RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

CMD ["sh", "-c", "while ! nc -z db 5432; do sleep 1; done && \
      python manage.py migrate && \
      python manage.py collectstatic --no-input && \
      python manage.py runserver 0.0.0.0:8000"]