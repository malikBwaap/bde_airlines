from fastapi import FastAPI
import os
import psycopg2
from pydantic import BaseModel

import socket

import requests

app = FastAPI()

#load_dotenv()  # loads from .env

def get_db():
    conn = psycopg2.connect(
        host=os.getenv("DB_PG_HOST", "db"),
        dbname=os.getenv("DB_PG_NAME"),
        user=os.getenv("DB_PG_USER"),
        password=os.getenv("DB_PG_PASSWORD")
    )
    return conn

API_KEY = "9aj2qh6kbg9ykydgh47frg5vp"
API_SECRET = "HXUX6GzpJR"

@app.get("/test_api")
async def test_api():
    return {"message": "This works!"}


@app.get("/get_db_env")
async def get_db_env():
    host=os.getenv("DB_PG_HOST", "db")
    ip_from_host = socket.gethostbyname(host)
    dbname=os.getenv("DB_PG_NAME"),
    user=os.getenv("DB_PG_USER"),
    password=os.getenv("DB_PG_PASSWORD")
    
    return {"dbname": dbname,
            "host": host,
            "user": user,
            "password": password}


@app.get("/simple_connect")
async def simple_connect():
    result = ""
    try:
        conn = get_db()
        result = "connected"
        print("✅ Connected to the database successfully!")

        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        print("Database version:", version)

        cur.close()
        conn.close()

    except Exception as e:
        result = "not connected"
        print("❌ Error:", e)
        
    return {"message": result,
            "version": version}


@app.get("/example_db_func")
async def example_db_func():
    string_ex = "example string"    
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS example (id SERIAL PRIMARY KEY, name TEXT);")
    cur.execute("INSERT INTO example (name) VALUES (%s) ON CONFLICT DO NOTHING;", ("Alice",))
    conn.commit()
    cur.execute("SELECT id, name FROM example LIMIT 1")
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return {"string_ex": string_ex, "id": row[0], "name": row[1]}
    else:
        return {"DB test failed."}
    

def get_access_token():
    API_KEY=os.getenv("LHT_API_KEY")
    API_SECRET=os.getenv("LHT_API_SECRET")
    url = "https://api.lufthansa.com/v1/oauth/token"
    payload = {
        "client_id": API_KEY,
        "client_secret": API_SECRET,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=payload)
    response.raise_for_status()

    data = response.json()
    return data.get("access_token")

@app.get("/example_lht_api_get_token")
async def example_lht_api_get_token():

    token = get_access_token()
    print("Got token:", token)
    
    return {"Token": token}

