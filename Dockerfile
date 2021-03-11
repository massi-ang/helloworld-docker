FROM python:3-alpine

COPY hello.py .

ENTRYPOINT ["python3", "hello.py"]

