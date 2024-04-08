from datetime import datetime
import pytz

# Get the current time in GMT
gmt = pytz.timezone('GMT')
gmt_time = datetime.now(gmt)

print("Current time in GMT is:", gmt_time.strftime('%Y-%m-%d %H:%M:%S'))
