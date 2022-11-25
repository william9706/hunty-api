FROM python:3.8
COPY . /app
WORKDIR /app/
RUN python3 -m pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0","--port", "8000"]
