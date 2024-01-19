FROM python:3.12.1-alpine


WORKDIR /app


EXPOSE 8000
COPY requirements.txt .



RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


CMD ["python", "main.py"]
