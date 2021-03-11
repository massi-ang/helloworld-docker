FROM public.ecr.aws/g9w5z2o2/python:3-alpine 

COPY hello.py .

ENTRYPOINT ["python3", "hello.py"]

