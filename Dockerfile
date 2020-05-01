FROM python:3-slim

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "hans.py"]
