FROM python:3.10.0

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY src src/

ENTRYPOINT [ "python3", "-m", "src.main"]
