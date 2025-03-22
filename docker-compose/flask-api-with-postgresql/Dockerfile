FROM python:3.9

WORKDIR /api

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY app.py .
ENTRYPOINT ["python3"]
CMD ["app.py"]