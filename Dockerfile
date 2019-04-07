FROM python:3.6-alpine3.8

LABEL maintainer="Kyunghan (Paul) Lee <enigma@enigmatic.network>"

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "bot.py"]
