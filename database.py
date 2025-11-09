from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def save_article(title: str, url: str, pub_date: str, content: str):
    supabase.table("articles").insert({
        "title": title,
        "url": url,
        "pub_date": pub_date,
        "content": content
    }).execute()

def get_articles_by_date_range(start_date: str, end_date: str):
    return supabase.table("articles").select("*").gte("pub_date", start_date).lte("pub_date", end_date).execute()

def is_article_processed(title: str):
    result = supabase.table("processed_articles").select("*").eq("title", title).execute()
    return len(result.data) > 0

def mark_article_as_processed(title: str):
    supabase.table("processed_articles").insert({"title": title}).execute()