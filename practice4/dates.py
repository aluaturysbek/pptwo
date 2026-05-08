import datetime

# 1

today = datetime.datetime.now()

new_date = today - datetime.timedelta(days=5)

print(new_date)


# 2

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


# 3

now = datetime.datetime.now().replace(microsecond=0)

print(now)


# 4

date1 = datetime.datetime(2026, 5, 1, 10, 0, 0)
date2 = datetime.datetime(2026, 5, 8, 12, 30, 0)

difference = date2 - date1

print(difference.total_seconds())