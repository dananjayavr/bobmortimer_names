FROM alpine:latest

RUN apk update && apk upgrade
RUN apk add --no-cache python3 \
                       py3-pip \
                       gcc \
    && rm -rf /var/cache/apk/*

RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip3 install wheel

COPY requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

COPY main.py /main.py
COPY names.txt /names.txt

CMD ["uvicorn", "main:app","--host", "0.0.0.0"]