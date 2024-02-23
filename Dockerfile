# tubetranscript/Dockerfile

FROM python:3.10

WORKDIR /app

RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

#RUN git clone https://github.com/brianshin22/tubetranscript.git .
COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8080

HEALTHCHECK CMD curl --fail http://localhost:8080/_stcore/health

ENTRYPOINT ["streamlit", "run", "tube_transcript.py", "--server.port=8080", "--server.address=0.0.0.0"]