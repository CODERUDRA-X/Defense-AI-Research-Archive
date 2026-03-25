import datetime

date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open('README.md', 'a', encoding='utf-8') as f:
    f.write(f"\n* Bot is alive and working! Time: {date_str}\n")
