import os
from dotenv import load_dotenv
from supabase import create_client, Client  

load_dotenv()
supabase_url = os.getenv("SUPABASE_API_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY")

print(f"Supabase URL: {supabase_url}")
print(f"Supabase Key: {supabase_key}")

if not supabase_url or not supabase_key:
    raise ValueError("Supabase URL or Service Key not found in environment variables.")

supabase: Client = create_client(supabase_url, supabase_key)
print("Supabase client created successfully.")