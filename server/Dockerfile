FROM python:slim
WORKDIR /app/
RUN pip install fastapi "uvicorn[standard]"
COPY . .
CMD ["python", "thats_so_server.py"]