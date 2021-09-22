FROM alpine:latest

RUN apk add --no-cache python3 \
    py3-pip

WORKDIR /app

COPY src .

RUN pip3 install -r requirements.txt && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate

CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8888" ]