from datetime import datetime, date
from pyscript import display
import asyncio

def format_date(dateToFormat):
    fmt = "%m/%d/%Y, %H:%M:%S"
    return f"{dateToFormat:{fmt}}"

async def countdown():
    ending_date = datetime(2025,8,15,0,0,0)
    event_name = "the CodeMash 2026 CFP Opening"
    display(event_name, target="eventName")
    display(format_date(ending_date),target="endingDate",append=False)
    while True:
        await asyncio.sleep(1)
        starting_date = datetime.now()
        td = ending_date - starting_date
        days, hours, minutes, seconds = td.days, td.seconds // 3600, td.seconds // 60 % 60, (td.seconds % 60)
        display(days, target="days", append=False)
        display(hours, target="hours", append=False)
        display(minutes, target="minutes", append=False)
        display(seconds, target="seconds", append=False)
        td = ending_date - starting_date



await countdown()