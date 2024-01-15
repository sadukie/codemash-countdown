from datetime import datetime, date
from pyscript import display
import asyncio

def format_date(dateToFormat):
    fmt = "%m/%d/%Y, %H:%M:%S"
    return f"{dateToFormat:{fmt}}"

async def countdown():
    codemash_date = datetime(2025,1,14,8,0,0)
    while True:
        await asyncio.sleep(1)
        td = (codemash_date - datetime.now())
        days, hours, minutes, seconds = td.days, td.seconds // 3600, td.seconds // 60 % 60, (td.seconds % 60)
        display(format_date(codemash_date),target="codemashDate",append=False)
        display(days, target="days", append=False)
        display(hours, target="hours", append=False)
        display(minutes, target="minutes", append=False)
        display(seconds, target="seconds", append=False)


await countdown()
