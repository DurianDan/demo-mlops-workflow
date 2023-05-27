FROM python:3.9.13-bullseye

COPY api api

COPY requirements.txt requirements.txt

RUN apt update -y && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

CMD [ "uvicorn", "api:main", "--reload" ]
