
import os
from dotenv import load_dotenv, find_dotenv
from supabase import create_client

env_path = find_dotenv(usecwd=True)
print("Environment file found:", env_path)

load_dotenv(env_path, override=True)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print("Project URL:", url)
print("Key prefix:", key[:15] if key else "MISSING")
print("Key length:", len(key) if key else 0)

if not url or not key:
    raise ValueError("Missing Supabase credentials")

supabase = create_client(url, key)

print("SafeAI connected to Supabase successfully!")
