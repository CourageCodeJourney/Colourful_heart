from datetime import datetime
import pytz

# Get the current time in a specific timezone
timezone_name = 'America/New_York'
local_timezone = pytz.timezone(timezone_name)
local_time = datetime.now(local_timezone)

print(f"Current time in {timezone_name} is:", local_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
