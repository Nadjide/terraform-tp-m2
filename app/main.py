import psycopg2
import redis
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2.extras import RealDictCursor

app = FastAPI()

# CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        cursor_factory=RealDictCursor
    )

@app.get('/')
async def get_etudiants():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        etudiants = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")
        return []
    
    result = []
    try:
        r = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True, socket_connect_timeout=1)
        # Check connection
        r.ping()
        redis_available = True
    except:
        redis_available = False

    for etudiant in etudiants:
        views = None
        if redis_available:
            try:
                views = r.incr(f"etudiant:{etudiant['id']}:views")
            except Exception:
                views = None
        
        result.append({
            "nom": etudiant['nom'],
            "promo": etudiant['promo'],
            "views": views
        })
        
    return result