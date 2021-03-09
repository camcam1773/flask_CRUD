FROM python:3.8-alpine

WORKDIR /crud
ADD app.py .
ADD requirements.txt .
ADD ./templates ./templates/

RUN pip install -r requirements.txt

expose 8080
CMD [ "python", "./app.py" ]