from datetime import datetime, timedelta
import pytz

# Get the current time in the local timezone
local_timezone = pytz.timezone('Your/Local/Timezone')  # Replace with your local timezone
current_time = datetime.now(local_timezone)

# Add 5 hours to the current time
final_time = current_time + timedelta(hours=5)

# Display the final time and timezone
print("Current Time (Local):", current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
print("Final Time (Local + 5 hours):", final_time.strftime("%Y-%m-%d %H:%M:%S %Z%z"))
