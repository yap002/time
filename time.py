import datetime
import pytz

# Get the current date and time in UTC
utc_now = datetime.datetime.now(pytz.UTC)
print("UTC:", utc_now)

# Convert UTC time to a specific time zone
target_timezone = pytz.timezone('America/New_York')
ny_time = utc_now.astimezone(target_timezone)
print("New York time:", ny_time)

# Get a list of available time zones
timezones = pytz.all_timezones
print("Available time zones:", timezones)

import datetime
from zoneinfo import ZoneInfo

# Get the current date and time in UTC
utc_now = datetime.datetime.now(ZoneInfo("UTC"))
print("UTC:", utc_now)

# Convert UTC time to a specific time zone
target_timezone = ZoneInfo("America/New_York")
ny_time = utc_now.astimezone(target_timezone)
print("New York time:", ny_time)

# Get a list of available time zones
timezones = ZoneInfo.available_timezones()
print("Available time zones:", timezones)
