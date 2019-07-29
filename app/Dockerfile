FROM python:3.8.0b2-alpine3.10

ENV BIND_PORT 5000

COPY ./requirements.txt /requirements.txt
COPY ./app.py /app.py

RUN pip install -r /requirements.txt

EXPOSE $BIND_PORT

CMD ["python", "/app.py"]
