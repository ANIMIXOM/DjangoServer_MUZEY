FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# RUN chmod +x /usr/local/bin/gunicorn
RUN python manage.py migrate
# RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "MuzeyServer.wsgi:application"]