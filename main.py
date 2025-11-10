from datetime import datetime, timedelta
from database import get_articles_by_date_range
from analyzer import generate_summary
from telegram_bot import send_summary_to_channel

CHANNEL_ID = "@your_channel"

async def run_daily_summary():
    now = datetime.now()
    start = now - timedelta(days=1)
    articles = get_articles_by_date_range(start.isoformat(), now.isoformat())
    summary = generate_summary(articles.data, "день")
    await send_summary_to_channel(summary, CHANNEL_ID)

async def run_weekly_summary():
    now = datetime.now()
    start = now - timedelta(weeks=1)
    articles = get_articles_by_date_range(start.isoformat(), now.isoformat())
    summary = generate_summary(articles.data, "неделя")
    await send_summary_to_channel(summary, CHANNEL_ID)

async def run_monthly_summary():
    now = datetime.now()
    start = now - timedelta(weeks=1)
    articles = get_articles_by_date_range(start.isoformat(), now.isoformat())
    summary = generate_summary(articles.data, "неделя")
    await send_summary_to_channel(summary, CHANNEL_ID)

    async def run_half_year_summary():
    now = datetime.now()
    start = now - timedelta(weeks=1)
    articles = get_articles_by_date_range(start.isoformat(), now.isoformat())
    summary = generate_summary(articles.data, "неделя")
    await send_summary_to_channel(summary, CHANNEL_ID)

     async def run_yearly_summary():
    now = datetime.now()
    start = now - timedelta(weeks=1)
    articles = get_articles_by_date_range(start.isoformat(), now.isoformat())
    summary = generate_summary(articles.data, "неделя")
    await send_summary_to_channel(summary, CHANNEL_ID)
# Аналогично: run_monthly_summary, run_half_year_summary, run_yearly_summary
