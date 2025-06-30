# Shahanshahi Calendar (Imperial Calendar for Python)

A Persian Imperial (Shahanshahi) calendar system based on the Jalali calendar with extended date and time support.

## Features
- Convert between Gregorian and Imperial dates.
- Get current Imperial date and time.
- Supports Persian day names and historical festivals.

## Install
```bash
pip install shahanshahi_calendar
```
## Example
```python
from shahanshahi_calendar import ImperialDate

today = ImperialDate.today()
print(today)  # e.g. 2584-04-09
print(today.day_name_en) # e.g Azar
```
