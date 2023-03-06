FROM python:3.8-slim-buster

RUN apt-get update \
    && apt-get install -y gcc build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "streamlit.py", "--server.port", "8501"]