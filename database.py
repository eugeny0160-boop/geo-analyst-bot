# database.py

import asyncpg
import os
import json

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

async def save_article_to_db(original_text: str, analysis: dict):
    """
    Сохраняет статью и её анализ в таблицу 'articles' в Supabase.
    """
    conn = None
    try:
        conn = await asyncpg.connect(SUPABASE_URL + "?sslmode=require", password=SUPABASE_KEY)

        # Вставляем данные
        await conn.execute("""
            INSERT INTO articles (title, content, analysis, created_at)
            VALUES ($1, $2, $3, NOW())
        """, 
        analysis.get("title", "Без заголовка"), 
        original_text, 
        json.dumps(analysis))  # Сохраняем анализ как JSON

        print("✅ Статья сохранена в базу.")

    except Exception as e:
        print(f"❌ Ошибка сохранения в базу: {e}")
    finally:
        if conn:
            await conn.close()
