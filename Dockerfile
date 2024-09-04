FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add gcc g++ musl-dev libpq-dev libffi-dev unixodbc-dev

WORKDIR /app

# Allows docker to cache installed dependencies between builds
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
# COPY . /app

EXPOSE 8111

# RUN python manage.py migrate

CMD ["gunicorn", "--config", "gunicorn_config.py", "gestor.wsgi:application"]