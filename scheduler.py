from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_daily_summary, run_weekly_summary, run_monthly_summary, run_half_year_summary, run_yearly_summary
from config import TIMEZONE
import pytz

scheduler = BlockingScheduler(timezone=pytz.timezone(TIMEZONE))

# Ежедневно в 21:00
scheduler.add_job(run_daily_summary, 'cron', hour=21, minute=0, id='daily')
# Еженедельно в воскресенье в 21:00
scheduler.add_job(run_weekly_summary, 'cron', day_of_week='sun', hour=21, minute=0, id='weekly')
# Ежемесячно в 21:00 первого числа
scheduler.add_job(run_monthly_summary, 'cron', day=1, hour=21, minute=0, id='monthly')
# Полугодие: 1 января и 1 июля
scheduler.add_job(run_half_year_summary, 'cron', month='1,7', day=1, hour=21, minute=0, id='half_year')
# Год: 1 января
scheduler.add_job(run_yearly_summary, 'cron', month=1, day=1, hour=21, minute=0, id='yearly')

def start_scheduler():
    print("Scheduler started...")
    scheduler.start()