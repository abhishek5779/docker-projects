FROM python:3.9

WORKDIR /api

COPY requirements.txt app.py /api/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]