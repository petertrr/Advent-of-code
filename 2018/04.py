from datetime import datetime
import re

date_format = '%Y-%m-%d %H:%M'

class event_type:
    wake = -1
    sleep = -2
    id = 0

def event_from_message(message):
    if message == 'wakes up':
        return event_type.wake
    elif message == 'falls asleep':
        return event_type.sleep
    else:
        return int(re.findall(r'#(\d+)', message)[0])

events = {}
guards = {}

with open("04.input") as f:
    for line in (line.strip() for line in f.readlines()):
        timestamp, message = re.findall(r'\[(.*)\] (.*)$', line)[0]
        date = datetime.strptime(timestamp, date_format)
        event = event_from_message(message)
        if event > 0:
            guards.update({event: [0 for _ in range(60)]})
        events.update({date: event})

cur_id = -1
for date in sorted(events):
    cur_minute = date.minute
    if events[date] > 0:
        cur_id = events[date]
    elif events[date] == event_type.sleep:
        guards[cur_id][cur_minute] += 1
        prev_minute = cur_minute
    elif events[date] == event_type.wake:
        for i in range(cur_minute - 1, prev_minute, -1):
            guards[cur_id][i] += 1

# strategy 1
sleepy_guard = max(guards, key=lambda guard: sum(guards[guard]))
print(sleepy_guard * guards[sleepy_guard].index(max(guards[sleepy_guard])))

# strategy 2
sleepy_guard = max(guards, key=lambda guard: max(guards[guard]))
print(sleepy_guard * guards[sleepy_guard].index(max(guards[sleepy_guard])))
