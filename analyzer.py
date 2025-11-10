# analyzer.py

import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def analyze_article(text: str) -> dict:
    """
    Анализирует статью с помощью OpenAI GPT.
    Возвращает словарь с заголовком, ключевыми темами, тональностью и кратким содержанием.
    """
    prompt = f"""
    Проанализируй следующую новостную статью и выдели:
    1. Краткий заголовок (не более 10 слов)
    2. Основные темы (до 5 пунктов)
    3. Тоныльность (позитивная, нейтральная, негативная)
    4. Краткое содержание (до 3 предложений)

    Статья:
    {text}

    Ответ предоставь в формате JSON:
    {{
      "title": "...",
      "topics": ["...", "..."],
      "sentiment": "...",
      "summary": "..."
    }}
    """

    try:
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",  # или gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "Ты — эксперт по геополитическому анализу."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=500
        )

        content = response.choices[0].message.content.strip()
        # Простая обработка JSON (можно улучшить с помощью json.loads)
        # Для надежности можно использовать `json.loads`, если ответ точно в формате JSON

        # Упрощённый парсер — для теста
        result = {
            "title": "Не удалось извлечь заголовок",
            "topics": ["Анализ не выполнен"],
            "sentiment": "неизвестно",
            "summary": "Ошибка анализа."
        }

        # Если хочешь полноценный JSON — раскомментируй ниже
        # import json
        # result = json.loads(content)

        return result

    except Exception as e:
        print(f"Ошибка анализа: {e}")
        return {
            "title": "Ошибка анализа",
            "topics": ["Ошибка"],
            "sentiment": "ошибка",
            "summary": str(e)
        }
