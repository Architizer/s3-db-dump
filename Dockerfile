FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && \
    apt-get install -y postgresql && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "dump_db.py"]