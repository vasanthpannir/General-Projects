s = "07:05:45PM"


period = s[-2:]

# Extract the hour, minute, and second parts
hour = int(s[:2])
minute_second = s[2:8]

# Convert the time based on AM/PM rules
if period == "AM":
    if hour == 12:
        hour = 0  # 12 AM is 00 in 24-hour format
else:
    if hour != 12:
        hour += 12  # Convert PM hours to 24-hour format

print(f"{hour:02}{minute_second}")