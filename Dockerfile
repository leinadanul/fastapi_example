FROM python:3.10

WORKDIR /fastAPI_example

COPY ./requirements.txt /fastAPI_example/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastAPI_example/requirements.txt

COPY ./main.py /fastAPI_example/main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
