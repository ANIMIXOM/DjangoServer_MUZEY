FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py sqlflush
RUN python manage.py makemigrations --merge
RUN python manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "MuzeyServer.wsgi:application"]