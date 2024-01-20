FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]
# Comando para executar o servidor Django
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]