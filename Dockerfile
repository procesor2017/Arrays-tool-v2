FROM python:3.10

WORKDIR /src

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY .  .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]