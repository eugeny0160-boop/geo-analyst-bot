import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_summary(news_list: list, period: str) -> str:
    # Подготовка текста для LLM
    input_text = f"Создай аналитическую записку за {period}.\n\nНовости:\n"
    for news in news_list:
        input_text += f"- {news['title']} ({news['url']})\n"

    prompt = f"""
    Ты — ведущий международный аналитик-геополитик. Создай краткую аналитическую записку по следующим новостям.
    Объем: {get_length_by_period(period)} знаков.
    Акцент: влияние на Россию и мир.
    Используй стиль: нейтральный, профессиональный, с URL в формате [URL источника].
    Структура: Исполнительное резюме, ТОП-5 событий, Тематический анализ, Влияние на Россию, Прогнозы.
    Входные данные:
    {input_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
        temperature=0.3
    )
    return response.choices[0].message['content'].strip()

def get_length_by_period(period: str):
    mapping = {
        "день": "1500-2000",
        "неделя": "2000-4000",
        "месяц": "4000-8000",
        "6 месяцев": "8000-10000",
        "год": "10000+"
    }
    return mapping.get(period, "2000")