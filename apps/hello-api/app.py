import os
from flask import Flask
import redis

app = Flask(__name__)
db = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def home():
    visits = db.incr("visits")
    return f"Hello from Ashiq's homelab! Visits: {visits}\n"

@app.route("/health")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
