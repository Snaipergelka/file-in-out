FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.2/wait /wait
RUN chmod +x /wait

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR .
COPY . .
