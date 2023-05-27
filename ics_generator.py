import csv
from ics import Calendar, Event
from datetime import time, datetime, timedelta

# Read the CSV file
rows = []
with open('study.csv', newline='') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        if len(row) == 3:
            rows.append(row)
        else:
            print(f"Skipping invalid row: {row}")

# Create a new calendar
c = Calendar()

for row in rows:
    date, topic, estimated_hours = row
    e = Event()
    e.name = topic.strip()
    start_time = time(21, 0)  # 9 PM
    end_time = time(23, 0)  # 11 PM

    # Check if the day is a weekend
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    if date_obj.weekday() >= 5:  # 5 and 6 correspond to Saturday and Sunday
        start_time = time(17, 0)  # 5 PM
        end_time = time(21, 0)  # 9 PM

    e.begin = datetime.combine(date_obj, start_time)
    e.end = datetime.combine(date_obj, end_time)
    c.events.add(e)

# Write the calendar to an .ics file
with open('study_schedule.ics', 'w') as f:
    f.write(c.serialize())
