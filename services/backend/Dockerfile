FROM python:3.10

WORKDIR /src

COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY src /src/app
COPY src/modules/matrix_csv /src/app/modules/matrix_csv

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]