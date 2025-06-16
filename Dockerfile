FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python collectstatic -no--input

EXPOSE 8000

ENV PYTHONUNBUFFERED=1
ENV DJANDO_SETTINGS_MODULE=webstore.settings.production

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]