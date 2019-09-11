FROM python:3.7-alpine

ADD app.py /
ADD requirements.txt /
ADD ./templates /templates/

RUN pip install -r requirements.txt

expose 8080
CMD [ "python", "./app.py" ]