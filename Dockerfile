FROM python:3.13-alpine

LABEL org.opencontainers.image.source=https://github.com/camcam1773/flask_CRUD
LABEL org.opencontainers.image.description="Flask CRUD"

WORKDIR /crud
ADD app.py .
ADD wsgi.py .
ADD requirements.txt .
ADD ./templates templates/
ADD ./tests tests/

RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

expose 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--access-logfile", "-", "--workers", "3", "wsgi:app"]
