FROM python:slim

COPY requirements.txt /
RUN python -m pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 80
ENTRYPOINT ["./gunicorn.sh"]