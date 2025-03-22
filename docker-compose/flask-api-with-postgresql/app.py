import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

DB_NAME = os.getenv("POSTGRES_DB", "default_db")
DB_USER = os.getenv("POSTGRES_USER", "default_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "default_pass")
DB_HOST = "db"        #The service name in docker-compose

@app.route('/')
def home():
    return "Welcome to Flask Application"

@app.route('/health')
def healthcheck():
    return jsonify(status="healthy"), 200

@app.route('/db-status')
def db_check():
    """Check PostgreSql connection status"""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        conn.close()
        return "PostgreSQL is connected"
    except Exception as e:
        return f"Database connection failed : {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)