FROM python:slim
RUN pip install fastapi uvicorn
WORKDIR /app/
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]